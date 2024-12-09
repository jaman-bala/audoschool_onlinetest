import uuid
from fastapi import Form, UploadFile, File

from src.exeptions import QuestionNotFoundException
from src.models import QuestionOrm
from src.schemas.questions import QuestionPatch, QuestionAdd, QuestionAddRequest
from src.services.base import BaseService



class QuestionsService(BaseService):
    async def create_questions(
            self,
            title: str = Form(None),
            description: str = Form(None),
            ticket_id: uuid.UUID = Form(None),
            theme_id: uuid.UUID = Form(None),
            files: list[UploadFile] = File(None),
    ):
        filenames = []
        if files:
            for file in files:
                saved_filename = await self.db.questions.save_photo(file)
                filenames.append(saved_filename)

        new_question = QuestionAdd(
            title=title,
            description=description,
            ticket_id=ticket_id,
            theme_id=theme_id,
            files=filenames,
        )
        await self.db.questions.add(new_question)
        await self.db.commit()


    async def get_questions(self):
        questions = await self.db.questions.get_all()
        return questions

    async def patch_questions(
        self, question_id: uuid.UUID, data: QuestionPatch, exclude_unset: bool = False
    ):
        question = await self.db.questions.get_one_or_none(id=question_id)
        if not question:
            raise QuestionNotFoundException
        await self.db.questions.edit_patch(data, exclude_unset=exclude_unset, id=question_id)
        await self.db.commit()

    async def delete_question(self, question_id: uuid.UUID):
        await self.db.questions.delete(id=question_id)
        await self.db.commit()

    async def patch_questions_file(self, question_id: uuid.UUID, files: list[UploadFile] = File(None)):
        # Получаем вопрос из базы данных
        question = await self.db.questions.get_one_or_none(id=question_id)

        if not question:
            raise QuestionNotFoundException

        # Получаем новые файлы, если они есть
        if files:
            new_filenames = await self.db.questions.upload_put(files)
            # Если новые файлы есть, добавляем их
            question.files.extend(new_filenames)

        # Если файлов нет, оставляем старые
        await self.db.questions.update(question)
        await self.db.commit()

        return {"message": "Файлы успешно обновлены"}
