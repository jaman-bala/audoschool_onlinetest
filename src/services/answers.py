import uuid
from datetime import datetime

from src.exeptions import AnswerNotFoundException
from src.schemas.answers import AnswerAdd, AnswerPatch, AnswerAddRequest
from src.services.base import BaseService


class AnswersService(BaseService):
    async def create_answers(self, data: AnswerAddRequest):
        new_answer = AnswerAdd(
            title=data.title,
            is_correct=data.is_correct,
            question_id=data.question_id,
            created_date=datetime.utcnow(),
            updated_date=datetime.utcnow(),
        )
        await self.db.answers.add(new_answer)
        await self.db.commit()
        return new_answer

    async def get_answers(self):
        answers = await self.db.answers.get_all()
        return answers

    async def get_answer_id(self, answer_id: uuid.UUID):
        answer_id = await self.db.answers.get_one(id=answer_id)
        return answer_id

    async def get_answers_by_question_id(self, question_id: uuid.UUID):
        answers = await self.db.answers.get_answers_by_question_id(question_id=question_id)
        return answers

    async def patch_answers(
        self, answer_id: uuid.UUID, data: AnswerPatch, exclude_unset: bool = False
    ):
        answer = await self.db.answers.get_one_or_none(id=answer_id)
        if not answer:
            raise AnswerNotFoundException
        await self.db.answers.edit_patch(data, exclude_unset=exclude_unset, id=answer_id)
        await self.db.commit()

    async def delete_answer(self, answer_id: uuid.UUID):
        answer = await self.db.answers.get_one_or_none(id=answer_id)
        if not answer:
            raise AnswerNotFoundException
        await self.db.answers.delete(id=answer_id)
        await self.db.commit()
