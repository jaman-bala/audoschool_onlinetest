from src.models import TotalOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import TotalDataMapper


class TotalsRepository(BaseRepository):
    model = TotalOrm
    mapper = TotalDataMapper
