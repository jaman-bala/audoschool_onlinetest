from src.schemas.answers import AnswerAdd
from src.services.base import BaseService


class AnswersService(BaseService):
    async def create_answers(self, data: AnswerAdd):
        answers = await self.db.answers.add(data)
        await self.db.commit()
        return answers

    async def get_answers(self):
        answers = await self.db.answers.get_all()
        return answers
