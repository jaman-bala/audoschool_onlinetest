from src.exeptions import AllErrorHTTPException
from src.services.base import BaseService
from src.schemas.questions import QuestionAdd, QuestionAddRequest


class QuestionsService(BaseService):
    async def create_questions(self, data: QuestionAddRequest):
        ticket = await self.db.tickets.get_one(data.ticket_id)
        if not ticket:
            raise AllErrorHTTPException
        new_question = QuestionAdd(
            title=data.title,
            description=data.description,
            photo=data.photo,
            ticket_id=data.ticket_id,
        )
        self.db.questions.add(new_question)
        await self.db.commit()
        return new_question
