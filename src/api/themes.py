import uuid
from fastapi import APIRouter

from src.api.dependencies import DBDep, UserIdDep, RoleSuperuserDep
from src.exeptions import (
    ExpiredTokenException,
    ExpiredTokenHTTPException,
    RolesAdminException,
    ObjectNotFoundException,
    UserNotFoundException,
)
from src.schemas.themes import ThemeAddRequest, ThemePatch
from src.services.themes import ThemesService

router = APIRouter(prefix="/themes", tags=["Тема"])


@router.post("", summary="Создание темы")
async def create_theme(data: ThemeAddRequest, role_admin: RoleSuperuserDep, db: DBDep):
    if not role_admin:
        raise RolesAdminException
    await ThemesService(db).create_themes(data)
    return {"message": "Тема создана"}


@router.get("", summary="Запрос всех тем")
async def get_theme(current_data: UserIdDep, db: DBDep):
    try:
        themes = await ThemesService(db).get_theme()
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    return {"message": "Доступ разрешен", "data": themes}


@router.patch("/{theme_id}", summary="Частичное изминение данных")
async def patch_theme(
    theme_id: uuid.UUID, role_admin: RoleSuperuserDep, data: ThemePatch, db: DBDep
):
    if not role_admin:
        raise RolesAdminException
    try:
        await ThemesService(db).patch_theme(theme_id, data)
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    except ObjectNotFoundException:
        raise UserNotFoundException
    return {"message": "Данные частично изменены"}


@router.delete("/{theme_id}", summary="Удаление данных")
async def delete_theme(theme_id: uuid.UUID, role_admin: RoleSuperuserDep, db: DBDep):
    if not role_admin:
        raise RolesAdminException
    try:
        await ThemesService(db).delete_theme(theme_id)
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    except ObjectNotFoundException:
        raise UserNotFoundException
    return {"message": "Данные удалены"}
