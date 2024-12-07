from src.models import ExamOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import ExamDataMapper


class ExamsRepository(BaseRepository):
    model = ExamOrm
    mapper = ExamDataMapper
