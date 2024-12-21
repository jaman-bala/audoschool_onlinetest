import uuid

from fastapi import APIRouter, Response
from uuid import UUID

from src.api.dependencies import UserIdDep, DBDep, RoleSuperuserDep
from src.exeptions import (
    UserNotFoundException,
    ObjectNotFoundException,
    UserNotRegisteredHTTPException,
    IncorrectPasswordException,
    IncorrectPasswordHTTPException,
    ExpiredTokenException,
    ExpiredTokenHTTPException,
    RolesAdminHTTPException,
    RolesSuperuserHTTPException,
)
from src.schemas.users import (
    UserRequestLogin,
    UserRequestUpdatePassword,
    UserPatchRequest,
    UserRequestAdd,
    UserResponse,
)
from src.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["Авторизация и аутентификация"])


@router.post("/create", summary="Создание пользователя 👨🏽‍💻")
async def register_user(
    role_superuser: RoleSuperuserDep,
    data: UserRequestAdd,
    db: DBDep,
):
    if not role_superuser:
        raise RolesSuperuserHTTPException
    user = await AuthService(db).register_user(data)
    user_response = UserResponse(
        firstname=user.firstname,
        lastname=user.lastname,
        phone=user.phone,
        is_ready=user.is_ready,
        group_id=user.group_id,
        is_active=user.is_active,
        roles=user.roles,
    )

    return {"status": "Пользователь создан", "data": user_response}


@router.post("/login", summary="Вход в систему 👨🏽‍💻")
async def login_user(
    data: UserRequestLogin,
    response: Response,
    db: DBDep,
):
    try:
        result = await AuthService(db).login_user(data)
        access_token = result["access_token"]
        user_id = result["user_id"]
        refresh_token = AuthService(db).create_refresh_token(
            response, access_token, {"user_id": user_id}
        )
    except UserNotFoundException:
        raise UserNotRegisteredHTTPException
    except IncorrectPasswordException:
        raise IncorrectPasswordHTTPException
    response.set_cookie("access_token", access_token)
    response.set_cookie("refresh_token", refresh_token, httponly=True)
    return {"status": "Успешный вход", "access_token": access_token}


@router.get("/me", summary="Мой профиль 👨🏽‍💻")
async def get_me(
    current_data: UserIdDep,
    db: DBDep,
):
    try:
        users = await AuthService(db).get_me(current_data)
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    return {"message": "Доступ разрешен", "data": users}


@router.get("/get_users_by_id/{user_id}", summary="Запрос по ID user")
async def get_users_by_id(
    role_admin: RoleSuperuserDep,
    user_id: uuid.UUID,
    db: DBDep,
):
    if not role_admin:
        raise RolesAdminHTTPException
    try:
        await AuthService(db).get_by_users_id(user_id)
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    except ObjectNotFoundException:
        raise UserNotFoundException


@router.get("/get_all_users", summary="Вывод всех пользователей 👨🏽‍💻")
async def get_all_users(
    role_admin: RoleSuperuserDep,
    db: DBDep,
):
    if not role_admin:
        raise RolesAdminHTTPException
    try:
        return await AuthService(db).get_all_users()
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    except ObjectNotFoundException:
        raise UserNotFoundException


@router.delete("/logout", summary="Выход из системы 👨🏽‍💻")
async def logout_user(
    response: Response,
):
    response.delete_cookie("access_token")
    return {"message": "Выход из системы успешен"}


@router.patch("/update/{user_id}", summary="Частичное изменение 👨🏽‍💻")
async def update_user(
    user_id: UUID,
    role_admin: RoleSuperuserDep,
    db: DBDep,
    data: UserPatchRequest,
):
    if not role_admin:
        raise RolesAdminHTTPException
    try:
        await AuthService(db).patch_user(user_id, data)
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    except ObjectNotFoundException:
        raise UserNotFoundException
    return {"message": "Данные пользователя частично изменены"}


@router.delete("/{user_id}", summary="Удаление пользователя 👨🏽‍💻")
async def delete_user(user_id: uuid.UUID, role_admin: RoleSuperuserDep, db: DBDep):
    if not role_admin:
        raise RolesAdminHTTPException
    try:
        await AuthService(db).delete_user(user_id)
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    except ObjectNotFoundException:
        raise UserNotFoundException
    return {"message": "Пользователь удален"}


@router.put("/change_password/{user_id}", summary="Сброс пароля")
async def change_password(
    user_id: UUID,
    role_admin: RoleSuperuserDep,
    data: UserRequestUpdatePassword,
    db: DBDep,
):
    if not role_admin:
        raise RolesAdminHTTPException
    try:
        await AuthService(db).change_password(user_id, data)
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    return {"message": "Пароль успешно изменён"}


@router.get("/get_users_by_group_id/{group_id}", summary="Вывод пользователей по группам")
async def get_users_by_group_id(group_id: uuid.UUID, db: DBDep):
    users = await AuthService(db).get_users_by_group_id(group_id)
    return {"message": users}
