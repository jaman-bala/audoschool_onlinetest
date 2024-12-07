from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.schemas.tickets import TicketAddRequest
from src.services.tickets import TicketsService

router = APIRouter(prefix="/tickets", tags=["Билеты"])


@router.post("/create")
async def create_tickets(data: TicketAddRequest, db: DBDep):
    await TicketsService(db).create_tickets(data)
    return {
        "message": "Билет создан",
    }


@router.get("")
async def get_tickets(db: DBDep):
    return await TicketsService(db).get_tickets()
