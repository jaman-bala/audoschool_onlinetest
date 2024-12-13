import uuid
from fastapi import APIRouter

from src.api.dependencies import DBDep, RoleSuperuserDep
from src.exeptions import (
    RolesAdminHTTPException,
    ExpiredTokenException,
    ExpiredTokenHTTPException,
    ObjectNotFoundException,
    UserNotFoundException,
)
from src.schemas.reports import ReportAddRequest, ReportPatch
from src.services.reports import ReportsService

router = APIRouter(prefix="/reports", tags=["Отчёт"])


@router.post("", summary="Добавление отчёта")
async def create_report(
    data: ReportAddRequest,
    role_admin: RoleSuperuserDep,
    db: DBDep,
):
    if not role_admin:
        raise RolesAdminHTTPException
    await ReportsService(db).create_reports(data)
    return {"status": "Отчёт добавлен"}


@router.get("", summary="Запрос всех данных")
async def get_report(db: DBDep):
    return await ReportsService(db).get_reports()


@router.patch("/{report_id}", summary="Частичное изминение")
async def patch_report(
    report_id: uuid.UUID, role_admin: RoleSuperuserDep, data: ReportPatch, db: DBDep
):
    if not role_admin:
        raise RolesAdminHTTPException
    try:
        await ReportsService(db).patch_reports(report_id, data)
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    except ObjectNotFoundException:
        raise UserNotFoundException
    return {"message": "Данные частично изменены"}


@router.delete("/{report_id}", summary="Удаление отчёта")
async def delete_report(report_id: uuid.UUID, role_admin: RoleSuperuserDep, db: DBDep):
    if not role_admin:
        raise RolesAdminHTTPException
    try:
        await ReportsService(db).delete_reports(report_id)
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    except ObjectNotFoundException:
        raise UserNotFoundException
    return {"message": "Отчёт удален"}
