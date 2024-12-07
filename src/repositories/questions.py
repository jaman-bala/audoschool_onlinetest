from src.models.questions import QuestionOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import QuestionDataMapper


class QuestionsRepository(BaseRepository):
    model = QuestionOrm
    mapper = QuestionDataMapper
