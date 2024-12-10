import uuid
from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.schemas.themes import ThemeAddRequest, ThemePatch
from src.services.themes import ThemesService

router = APIRouter(prefix="/themes", tags=["Тема"])


@router.post("", summary="Создание темы")
async def create_theme(data: ThemeAddRequest, db: DBDep):
    await ThemesService(db).create_themes(data)
    return {"message": "Тема создана"}


@router.get("", summary="Запрос всех тем")
async def get_theme(db: DBDep):
    return await ThemesService(db).get_theme()


@router.patch("/{theme_id}", summary="Частичное изминение данных")
async def patch_theme(theme_id: uuid.UUID, data: ThemePatch, db: DBDep):
    await ThemesService(db).patch_theme(theme_id, data)
    return {"message": "Данные частично изменены"}


@router.delete("/{theme_id}", summary="Удаление данных")
async def delete_theme(theme_id: uuid.UUID, db: DBDep):
    await ThemesService(db).delete_theme(theme_id)
    return {"message": "Данные удалены"}
