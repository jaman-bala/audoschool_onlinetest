import uuid
from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.schemas.totals import TotalPatch, TotalAddRequest
from src.services.totals import TotalsService

router = APIRouter(prefix="/totals", tags=["Финальный отчёт"])


@router.post("", summary="Добавление финального отчёта")
async def create_total(data: TotalAddRequest, db: DBDep):
    await TotalsService(db).ctrate_totals(data)


@router.get("", summary="Запрос всех данных")
async def get_total(db: DBDep):
    return await TotalsService(db).get_totals()


@router.patch("/{total_id}", summary="Частичное изминение данных")
async def patch_total(total_id: uuid.UUID, data: TotalPatch, db: DBDep):
    await TotalsService(db).patch_totals(total_id, data)
    return {"message": "Данные частично изменены"}


@router.delete("/{total_id}", summary="Удаление данных")
async def delete_total(total_id: uuid.UUID, db: DBDep):
    await TotalsService(db).delete_totals(total_id)
    return {"message": "Данные удалены"}
