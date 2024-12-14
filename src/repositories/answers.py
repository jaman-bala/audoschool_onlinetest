from sqlalchemy import select

from src.models.answers import AnswerOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import AnswerDataMapper


class AnswersRepository(BaseRepository):
    model = AnswerOrm
    mapper = AnswerDataMapper

    async def get_answers_by_question_id(self, question_id: str):
        query = select(self.model).where(self.model.question_id == question_id)
        result = await self.session.execute(query)
        models = result.scalars().all()
        return models
