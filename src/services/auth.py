import jwt
import uuid

from uuid import UUID
from fastapi import Response
from passlib.context import CryptContext
from datetime import datetime, timezone, timedelta

from src.config import settings
from src.exeptions import (
    ObjectAlreadyExistsException,
    UserAlreadyExistsException,
    UserNotFoundException,
    IncorrectTokenHTTPException,
    InnAlreadyExistsException,
    IncorrectPasswordHTTPException,
    ExpiredTokenHTTPException,
)
from src.models import UsersOrm
from src.schemas.users import (
    UserAdd,
    UserUpdatePassword,
    UserPatchRequest,
    UserAddLogin,
    UserRequestAdd,
    UserUpdateInn,
)
from src.services.base import BaseService
from src.services.images import ImagesService


class AuthService(BaseService):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def create_access_token(self, user: UsersOrm) -> str:
        roles = [role.value for role in user.roles]
        data = {
            "user_id": str(user.id),
            "roles": roles,
        }
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        data["exp"] = expire
        print(f"Payload for token: {data}")

        encoded_jwt = jwt.encode(data, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        return encoded_jwt

    def create_refresh_token(self, response: Response, refresh_token: str, data: dict) -> str:
        data = {
            key: str(value) if isinstance(value, uuid.UUID) else value
            for key, value in data.items()
        }
        response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,
            max_age=60 * 60 * 24 * settings.REFRESH_TOKEN_EXPIRE_DAYS,  # срок жизни
            samesite="Lax",  # или "Strict"
            secure=True,  # Рекомендуется включать, если используется HTTPS
        )

        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        to_encode |= {"exp": expire}
        encoded_jwt = jwt.encode(
            to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
        )
        return encoded_jwt

    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def decode_access_token(self, token: str) -> dict:
        try:
            payload = jwt.decode(
                token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
            )
            return payload
        except jwt.ExpiredSignatureError:
            raise ExpiredTokenHTTPException
        except jwt.exceptions.DecodeError:
            raise IncorrectTokenHTTPException

    async def register_user(self, data: UserRequestAdd):
        existing_user = await self.db.users.get_one_or_none(inn=data.inn)
        if existing_user:
            raise InnAlreadyExistsException
        hashed_password = self.hash_password(data.password)
        new_user_data = UserAdd(
            inn=data.inn,
            name=data.name,
            surname=data.surname,
            middle_name=data.middle_name,
            phone_number=data.phone_number,
            address=data.address,
            email=data.email,
            hashed_password=hashed_password,
            birthday=data.birthday,
            groups=data.groups,
            categories=data.categories,
            date_from=data.date_from,
            date_to=data.date_to,
            price=data.price,
            is_active=data.is_active,
            admin=data.admin,
            user=data.user,
            created_date=datetime.utcnow(),
            updated_date=datetime.utcnow(),
        )
        try:
            await self.db.users.add(new_user_data)
            await self.db.commit()
        except ObjectAlreadyExistsException as exc:
            raise UserAlreadyExistsException from exc

    async def get_me(self, user_id: UUID):
        try:
            user = await self.db.users.get_one_or_none(id=user_id)
            images_service = ImagesService(self.db)
            if not user:
                raise UserNotFoundException
            user_images = await images_service.get_all_images(user.id)
            if user_images:
                user.avatar = user_images[0]["avatar"]
            else:
                user.avatar = None
        except jwt.exceptions.DecodeError:
            raise IncorrectTokenHTTPException
        return user

    async def login_user(self, data: UserAddLogin):
        user = await self.db.users.get_user_phone_number_with_hashed_password(
            phone_number=data.phone_number
        )
        if not user:
            raise InnAlreadyExistsException
        if not self.verify_password(data.password, user.hashed_password):
            raise IncorrectPasswordHTTPException
        access_token = self.create_access_token(user)
        return {"access_token": access_token, "user_id": str(user.id)}

    async def get_all_users(self):
        try:
            users = await self.db.users.get_all()
            images_service = ImagesService(self.db)
            if not users:
                raise UserNotFoundException
            for user in users:
                user_images = await images_service.get_all_images(user.id)
                if user_images:
                    user.avatar = user_images[0]["avatar"]
                else:
                    user.avatar = None
        except jwt.exceptions.DecodeError:
            raise IncorrectTokenHTTPException
        return users

    async def get_by_id(self, user_id: UUID):
        user = await self.db.users.get_one(id=user_id)
        if not user:
            raise UserNotFoundException
        return user

    async def put_user(self, user_id: UUID, data: UserUpdateInn):
        user = await self.db.users.get_one_or_none(id=user_id)
        if not user:
            raise UserNotFoundException
        await self.db.users.update(data, id=user_id)
        await self.db.commit()

    async def patch_user(self, user_id: UUID, data: UserPatchRequest, exclude_unset: bool = False):
        user = await self.db.users.get_one_or_none(id=user_id)
        if not user:
            raise UserNotFoundException
        await self.db.users.edit_patch(data, exclude_unset, id=user_id)
        await self.db.commit()

    async def change_password(self, user_id: UUID, data: UserUpdatePassword):
        user = await self.db.users.get_one(id=user_id)
        if not user:
            raise UserNotFoundException
        hashed_new_password = self.hash_password(data.new_password)
        await self.db.users.update_user_hashed_password(user_id, hashed_new_password)
        await self.db.commit()
