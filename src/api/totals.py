import uuid
from fastapi import APIRouter

from src.api.dependencies import DBDep, RoleSuperuserDep, UserIdDep
from src.exeptions import (
    RolesAdminHTTPException,
    ExpiredTokenException,
    ExpiredTokenHTTPException,
    ObjectNotFoundException,
    UserNotFoundException,
)
from src.schemas.totals import TotalPatch, TotalAddRequest
from src.services.totals import TotalsService

router = APIRouter(prefix="/totals", tags=["Финальный отчёт"])


@router.post("", summary="Добавление финального отчёта")
async def create_total(data: TotalAddRequest, role_admin: RoleSuperuserDep, db: DBDep):
    if not role_admin:
        raise RolesAdminHTTPException
    await TotalsService(db).ctrate_totals(data)
    return {"message": "Финальный отчёт создан"}


@router.get("", summary="Запрос всех данных")
async def get_total(current_data: UserIdDep, db: DBDep):
    return await TotalsService(db).get_totals()


@router.patch("/{total_id}", summary="Частичное изминение данных")
async def patch_total(
    total_id: uuid.UUID, role_admin: RoleSuperuserDep, data: TotalPatch, db: DBDep
):
    if not role_admin:
        raise RolesAdminHTTPException
    try:
        await TotalsService(db).patch_totals(total_id, data)
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    except ObjectNotFoundException:
        raise UserNotFoundException
    return {"message": "Данные частично изменены"}


@router.delete("/{total_id}", summary="Удаление данных")
async def delete_total(total_id: uuid.UUID, role_admin: RoleSuperuserDep, db: DBDep):
    if not role_admin:
        raise RolesAdminHTTPException
    try:
        await TotalsService(db).delete_totals(total_id)
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    except ObjectNotFoundException:
        raise UserNotFoundException
    return {"message": "Данные удалены"}
