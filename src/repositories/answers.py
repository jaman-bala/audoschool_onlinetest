from src.models.answers import AnswerOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import AnswerDataMapper


class AnswersRepository(BaseRepository):
    model = AnswerOrm
    mapper = AnswerDataMapper
