import uuid
from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.schemas.group import GroupAddRequest, GroupPatch
from src.services.group import GroupsService

router = APIRouter(prefix="/group", tags=["Группы"])


@router.post("", summary="Создание группы")
async def create_group(data: GroupAddRequest, db: DBDep):
    await GroupsService(db).create_group(data)
    return {"message": "Группа создан"}

@router.get("", summary="Запрос всех групп")
async def get_group(db: DBDep):
    return await GroupsService(db).get_group()

@router.patch("/group_id")
async def patch_group(grop_id: uuid.UUID, data: GroupPatch, db: DBDep):
    await GroupsService(db).patch_group(grop_id, data)
    return {"message": "Данные честично изменены"}

@router.delete("/{group_id")
async def delete_group(group_id: uuid.UUID, db: DBDep):
    await GroupsService(db).delete_group(group_id)
    return {"message": "Данные удалены"}