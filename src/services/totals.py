import uuid
from datetime import datetime

from src.exeptions import TotalNotFoundException
from src.schemas.totals import TotalAddRequest, TotalAdd, TotalPatch
from src.services.base import BaseService


class TotalsService(BaseService):
    async def ctrate_totals(self, data: TotalAddRequest):
        new_total = TotalAdd(
            user_id=data.user_id,
            points=data.points,
            date_from=data.date_from,
            date_end=data.date_end,
            created_date=datetime.utcnow(),
            updated_date=datetime.utcnow(),
        )
        await self.db.totals.add(new_total)
        await self.db.commit()
        return new_total

    async def get_totals(self):
        totals = await self.db.totals.get_all()
        return totals

    async def patch_totals(
        self, total_id: uuid.UUID, data: TotalPatch, exclude_unset: bool = False
    ):
        total = await self.db.totals.get(total_id)
        if not total:
            raise TotalNotFoundException
        await self.db.totals.edit_patch(data, exclude_unset=exclude_unset, id=total_id)
        await self.db.commit()

    async def delete_totals(self, total_id: uuid.UUID):
        await self.db.totals.delete(id=total_id)
        await self.db.commit()
