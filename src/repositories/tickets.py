from sqlalchemy import select

from src.models import TicketOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import TicketDataMapper


class TicketsRepository(BaseRepository):
    model = TicketOrm
    mapper = TicketDataMapper

    async def get_one(self, ticket_id: int):
        query = select(self.model).filter_by(id=ticket_id)
        result = await self.session.execute(query)
        model = result.scalars().one()
        return self.mapper.map_to_domain_entity(model)
