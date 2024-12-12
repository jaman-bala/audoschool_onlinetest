import uuid
from fastapi import APIRouter

from src.api.dependencies import DBDep, RoleSuperuserDep, UserIdDep
from src.exeptions import (
    RolesAdminException,
    ExpiredTokenException,
    ExpiredTokenHTTPException,
    ObjectNotFoundException,
    UserNotFoundException,
)
from src.schemas.tickets import TicketAddRequest, TicketPatch
from src.services.tickets import TicketsService

router = APIRouter(prefix="/tickets", tags=["Билеты"])


@router.post("", summary="Добавить билет")
async def create_tickets(data: TicketAddRequest, role_admin: RoleSuperuserDep, db: DBDep):
    if not role_admin:
        raise RolesAdminException
    await TicketsService(db).create_tickets(data)
    return {
        "message": "Билет создан",
    }


@router.get("", summary="Запрос всех данных")
async def get_tickets(current_data: UserIdDep, db: DBDep):
    return await TicketsService(db).get_tickets()


@router.patch("/{ticket_id}", summary="Частичное изминение данных")
async def patch_ticket(
    ticket_id: uuid.UUID, role_admin: RoleSuperuserDep, data: TicketPatch, db: DBDep
):
    if not role_admin:
        raise RolesAdminException
    try:
        await TicketsService(db).patch_ticket(ticket_id, data)
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    except ObjectNotFoundException:
        raise UserNotFoundException
    return {"message": "Данные частично изменены"}


@router.delete("/{ticket_id}")
async def delete_ticket(ticket_id: uuid.UUID, role_admin: RoleSuperuserDep, db: DBDep):
    if not role_admin:
        raise RolesAdminException
    try:
        await TicketsService(db).delete_ticket(ticket_id)
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    except ObjectNotFoundException:
        raise UserNotFoundException
    return {"message": "Билет удален"}
