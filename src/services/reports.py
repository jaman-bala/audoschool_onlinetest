import uuid
from datetime import datetime

from src.exeptions import ReportNotFoundException
from src.schemas.reports import ReportAddRequest, ReportAdd, ReportPatch
from src.services.base import BaseService


class ReportsService(BaseService):
    async def create_reports(self, data: ReportAddRequest):
        new_reports = ReportAdd(
            user_id=data.user_id,
            ticket_id=data.ticket_id,
            theme_id=data.theme_id,
            points=data.points,
            date_from=data.date_from,
            date_end=data.date_end,
            created_date=datetime.utcnow(),
            updated_date=datetime.utcnow(),
        )
        await self.db.reports.add(new_reports)
        await self.db.commit()
        return new_reports

    async def get_reports(self):
        reports = await self.db.reports.get_all()
        return reports

    async def patch_reports(
        self, report_id: uuid.UUID, data: ReportPatch, exclude_unset: bool = False
    ):
        report = await self.db.reports.get_one_or_none(id=report_id)
        if not report:
            raise ReportNotFoundException
        await self.db.reports.edit_patch(data, exclude_unset=exclude_unset, id=report_id)
        await self.db.commit()

    async def delete_reports(self, report_id: uuid.UUID):
        await self.db.reports.delete(id=report_id)
        await self.db.commit()
