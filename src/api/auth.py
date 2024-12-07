from fastapi import APIRouter, Response
from uuid import UUID

from src.api.dependencies import UserIdDep, DBDep, RoleSuperuserDep, RoleAdminDep
from src.exeptions import (
    UserNotFoundException,
    UserAlreadyExistsException,
    UserEmailAlreadyExistsHTTPException,
    InnAlreadyExistsException,
    InnAlreadyExistsHTTPException,
    ObjectNotFoundException,
    UserNotRegisteredHTTPException,
    IncorrectPasswordException,
    IncorrectPasswordHTTPException,
    ExpiredTokenException,
    ExpiredTokenHTTPException,
    RolesAdminException,
)
from src.schemas.users import (
    UserRequestLogin,
    UserUpdateRequest,
    UserRequestUpdatePassword,
    UserPatchRequest,
    UserRequestAdd,
)
from src.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["Авторизация и аутентификация"])


@router.post("/create", summary="Создание пользователя 👨🏽‍💻")
async def register_user(
    # role_superuser: RoleSuperuserDep,
    data: UserRequestAdd,
    db: DBDep,
):
    # if not role_superuser:
    #     raise RolesSuperuserException
    try:
        await AuthService(db).register_user(data)
    except UserAlreadyExistsException:
        raise UserEmailAlreadyExistsHTTPException
    except InnAlreadyExistsException:
        raise InnAlreadyExistsHTTPException
    return {"status": "Пользователь создан"}


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
    response.set_cookie("refresh_token", refresh_token)
    return {"status": "Успешный вход", "access_token": access_token, "refresh_token": refresh_token}


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


@router.get("/get_all_users", summary="Вывод всех пользователей 👨🏽‍💻")
async def get_all_users(
    role_admin: RoleAdminDep,
    db: DBDep,
):
    if not role_admin:
        raise RolesAdminException
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


@router.put("/{user_id}", summary="Измнить данные у пользователя 👨🏽‍💻")
async def put_user(
    user_id: UUID,
    db: DBDep,
    data: UserUpdateRequest,
    role_admin: RoleAdminDep,
):
    if not role_admin:
        raise RolesAdminException
    try:
        await AuthService(db).put_user(user_id, data)
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    except ObjectNotFoundException:
        raise UserNotFoundException
    return {"message": "Данные пользователя изменены"}


@router.put("/change_password/{user_id}", summary="Сброс пароля")
async def change_password(
    user_id: UUID,
    role_admin: RoleAdminDep,
    data: UserRequestUpdatePassword,
    db: DBDep,
):
    if not role_admin:
        raise RolesAdminException
    try:
        await AuthService(db).change_password(user_id, data)
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    return {"message": "Пароль успешно изменён"}


@router.patch("/update/{user_id}", summary="Частичное изменение 👨🏽‍💻")
async def update_user(
    user_id: UUID,
    role_admin: RoleAdminDep,
    db: DBDep,
    data: UserPatchRequest,
):
    if not role_admin:
        raise RolesAdminException
    try:
        await AuthService(db).patch_user(user_id, data)
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    except ObjectNotFoundException:
        raise UserNotFoundException
    return {"message": "Данные пользователя частично изменены"}
