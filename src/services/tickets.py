from datetime import datetime

from src.schemas.tickets import TicketAdd, TicketAddRequest
from src.services.base import BaseService


class TicketsService(BaseService):
    async def create_tickets(self, data: TicketAddRequest):
        create_ticket = TicketAdd(
            title=data.title,
            description=data.description,
            created_date=datetime.utcnow(),
            updated_date=datetime.utcnow(),
        )
        await self.db.tickets.add(create_ticket)
        await self.db.commit()

    async def get_tickets(self):
        tickets = await self.db.tickets.get_all()
        return tickets
