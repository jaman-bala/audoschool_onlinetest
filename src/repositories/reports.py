from src.models.reports import ReportOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import ReportDataMapper


class ReportsRepository(BaseRepository):
    model = ReportOrm
    mapper = ReportDataMapper
