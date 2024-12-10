import uuid
from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.schemas.payments import PaymentAddRequest, PaymentPatch
from src.services.payments import PaymentsService

router = APIRouter(prefix="/payments", tags=["Платёж"])


@router.post("", summary="Добавить платёж")
async def create_payments(data: PaymentAddRequest, db: DBDep):
    await PaymentsService(db).create_payments(data)
    return {"message": "Платёж создан"}


@router.get("", summary="Запрос всех данных")
async def get_payments(db: DBDep):
    return await PaymentsService(db).get_payments()


@router.patch("/{payment_id}", summary="Частичное изминение данных")
async def patch_payments(payment_id: uuid.UUID, data: PaymentPatch, db: DBDep):
    await PaymentsService(db).patch_payments(payment_id, data)
    return {"message": "Данные частично изменены"}


@router.delete("/{payment_id}", summary="Удаление данных")
async def delete_payments(payment_id: uuid.UUID, db: DBDep):
    await PaymentsService(db).delete_payments(payment_id)
    return {"message": "Данные удалены"}
