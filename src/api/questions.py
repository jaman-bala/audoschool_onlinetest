import uuid
from typing import List
from fastapi import APIRouter, UploadFile, File, Form

from src.api.dependencies import DBDep
from src.schemas.questions import QuestionPatch, QuestionAddRequest
from src.services.questions import QuestionsService

router = APIRouter(prefix="/questions", tags=["Вопросы"])


@router.post("/create", summary="Создание билетов")
async def create_question(
        db: DBDep,
        title: str = Form(None),
        description: str = Form(None),
        ticket_id: uuid.UUID = Form(None),
        theme_id: uuid.UUID = Form(None),
        files: List[UploadFile] = File(None),
):
    await QuestionsService(db).create_questions(
        title=title, description=description, ticket_id=ticket_id, theme_id=theme_id, files=files
    )
    return {"message": "Вопрос создан"}


@router.get("", summary="Запрос всех вопросов")
async def get_questions(db: DBDep):
    return await QuestionsService(db).get_questions()


@router.patch("/{question_id}", summary="Частичное изминение данных")
async def patch_question(question_id: uuid.UUID, data: QuestionPatch, db: DBDep):
    await QuestionsService(db).patch_questions(question_id, data)
    return {"message": "Данные частично изменены"}


@router.delete("/{question_id}", summary="Удаление вопроса")
async def delete_question(question_id: uuid.UUID, db: DBDep):
    await QuestionsService(db).delete_question(question_id)
    return {"message": "Вопрос удален"}


@router.put("/{question_id}", summary="Обновление файлов для вопроса")
async def put_question_files(
    db: DBDep,
    question_id: uuid.UUID,
    files: List[UploadFile] = File(None),
):
    await QuestionsService(db).patch_questions_file(question_id, files)
    return {"message": "Файлы успешно обновлены"}