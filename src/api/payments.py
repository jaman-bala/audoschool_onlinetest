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
from src.schemas.payments import PaymentAddRequest, PaymentPatch
from src.services.payments import PaymentsService

router = APIRouter(prefix="/payments", tags=["Платёж"])


@router.post("", summary="Добавить платёж")
async def create_payments(
        data: PaymentAddRequest,
    #    role_admin: RoleSuperuserDep,
        db: DBDep):
#    if not role_admin:
#        raise RolesAdminHTTPException
    payments = await PaymentsService(db).create_payments(data)
    return {"message": "Платёж создан", "data": payments}


@router.get("", summary="Запрос всех данных")
async def get_payments(db: DBDep):
    return await PaymentsService(db).get_payments()

@router.get("/{payment_id}", summary="Запрос по ID")
async def get_by_payments_id(
        #    current_data: UserIdDep,
        payment_id: uuid.UUID,
        db: DBDep
):
    return await PaymentsService(db).get_payment_by_id(payment_id)


@router.patch("/{payment_id}", summary="Частичное изминение данных")
async def patch_payments(
    payment_id: uuid.UUID, role_admin: RoleSuperuserDep, data: PaymentPatch, db: DBDep
):
    if not role_admin:
        raise RolesAdminHTTPException
    try:
        await PaymentsService(db).patch_payments(payment_id, data)
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    except ObjectNotFoundException:
        raise UserNotFoundException
    return {"message": "Данные частично изменены"}


@router.delete("/{payment_id}", summary="Удаление данных")
async def delete_payments(payment_id: uuid.UUID, role_admin: RoleSuperuserDep, db: DBDep):
    if not role_admin:
        raise RolesAdminHTTPException
    try:
        await PaymentsService(db).delete_payments(payment_id)
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    except ObjectNotFoundException:
        raise UserNotFoundException
    return {"message": "Данные удалены"}
