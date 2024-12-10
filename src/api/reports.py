import uuid
from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.schemas.reports import ReportAddRequest
from src.services.reports import ReportsService

router = APIRouter(prefix="/reports", tags=["Отчёт"])


@router.post("", summary="Добавление отчёта")
async def create_report(
    data: ReportAddRequest,
    db: DBDep,
):
    await ReportsService(db).create_reports(data)
    return {"status": "Отчёт добавлен"}


@router.get("", summary="Запрос всех данных")
async def get_report(db: DBDep):
    return await ReportsService(db).get_reports()


@router.patch("/{report_id}", summary="Частичное изминение")
async def patch_report(report_id: uuid.UUID, data: ReportAddRequest, db: DBDep):
    await ReportsService(db).patch_reports(report_id, data)
    return {"message": "Данные частично изменены"}


@router.delete("/{report_id}", summary="Удаление отчёта")
async def delete_report(report_id: uuid.UUID, db: DBDep):
    await ReportsService(db).delete_reports(report_id)
    return {"message": "Отчёт удален"}
