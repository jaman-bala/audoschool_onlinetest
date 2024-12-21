import uuid
from typing import List
from fastapi import APIRouter, UploadFile, File, Form

from src.api.dependencies import DBDep, RoleSuperuserDep
from src.exeptions import (
    RolesAdminHTTPException,
    ExpiredTokenException,
    ExpiredTokenHTTPException,
    ObjectNotFoundException,
    UserNotFoundException,
)
from src.schemas.questions import QuestionPatch
from src.services.questions import QuestionsService

router = APIRouter(prefix="/questions", tags=["Вопросы"])


@router.post("/create", summary="Создание билетов")
async def create_question(
    db: DBDep,
    role_admin: RoleSuperuserDep,
    title: str = Form(None),
    description: str = Form(None),
    ticket_id: uuid.UUID = Form(None),
    theme_id: uuid.UUID = Form(None),
    files: List[UploadFile] = File(None),
):
    if not role_admin:
        raise RolesAdminHTTPException
    await QuestionsService(db).create_questions(
        title=title, description=description, ticket_id=ticket_id, theme_id=theme_id, files=files
    )
    return {"message": "Вопрос создан"}


@router.get("", summary="Запрос всех вопросов")
async def get_questions(db: DBDep):
    return await QuestionsService(db).get_questions()


@router.get("/by-ticket/{ticket_id}", summary="Получить вопросы по ticket_id")
async def get_questions_by_ticket_id(ticket_id: uuid.UUID, db: DBDep):
    questions = await QuestionsService(db).get_questions_by_ticket_id(ticket_id)
    return {"questions": questions}


@router.patch("/{question_id}", summary="Частичное изминение данных")
async def patch_question(
    question_id: uuid.UUID, role_admin: RoleSuperuserDep, data: QuestionPatch, db: DBDep
):
    if not role_admin:
        raise RolesAdminHTTPException
    try:
        await QuestionsService(db).patch_questions(question_id, data)
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    except ObjectNotFoundException:
        raise UserNotFoundException
    return {"message": "Данные частично изменены"}


@router.delete("/{question_id}", summary="Удаление вопроса")
async def delete_question(question_id: uuid.UUID, role_admin: RoleSuperuserDep, db: DBDep):
    if not role_admin:
        raise RolesAdminHTTPException
    try:
        await QuestionsService(db).delete_question(question_id)
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    except ObjectNotFoundException:
        raise UserNotFoundException
    return {"message": "Вопрос удален"}


@router.put("/{question_id}", summary="Обновление файлов для вопроса")
async def put_question_files(
    db: DBDep,
    role_admin: RoleSuperuserDep,
    question_id: uuid.UUID,
    files: List[UploadFile] = File(None),
):
    if not role_admin:
        raise RolesAdminHTTPException
    try:
        await QuestionsService(db).patch_questions_file(question_id, files)
    except ExpiredTokenException:
        raise ExpiredTokenHTTPException
    except ObjectNotFoundException:
        raise UserNotFoundException
    return {"message": "Файлы успешно обновлены"}


@router.get("/random")
async def get_random_question(db: DBDep):
    return await QuestionsService(db).get_random_questions()
