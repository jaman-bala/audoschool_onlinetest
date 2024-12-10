import uuid
from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.schemas.tickets import TicketAddRequest, TicketPatch
from src.services.tickets import TicketsService

router = APIRouter(prefix="/tickets", tags=["Билеты"])


@router.post("", summary="Добавить билет")
async def create_tickets(data: TicketAddRequest, db: DBDep):
    await TicketsService(db).create_tickets(data)
    return {
        "message": "Билет создан",
    }


@router.get("", summary="Запрос всех данных")
async def get_tickets(db: DBDep):
    return await TicketsService(db).get_tickets()


@router.patch("/{ticket_id}", summary="Частичное изминение данных")
async def patch_ticket(ticket_id: uuid.UUID, data: TicketPatch, db: DBDep):
    await TicketsService(db).patch_ticket(ticket_id, data)
    return {"message": "Данные частично изменены"}


@router.delete("/{ticket_id}")
async def delete_ticket(ticket_id: uuid.UUID, db: DBDep):
    await TicketsService(db).delete_ticket(ticket_id)
    return {"message": "Билет удален"}
