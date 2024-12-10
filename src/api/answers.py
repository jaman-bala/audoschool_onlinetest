import uuid
from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.services.answers import AnswersService
from src.schemas.answers import AnswerAddRequest, AnswerPatch

router = APIRouter(prefix="/answers", tags=["Ответы"])


@router.post("", summary="Добавление ответа")
async def add_answers(
    data: AnswerAddRequest,
    db: DBDep,
):
    await AnswersService(db).create_answers(data)
    return {"status": "Ответ добавлен"}


@router.get("")
async def get_answers(db: DBDep):
    return await AnswersService(db).get_answers()


@router.patch("/{answer_id}")
async def update_answer(answer_id: uuid.UUID, data: AnswerPatch, db: DBDep):
    await AnswersService(db).patch_answers(answer_id, data)
    return {"message": "Данные честично изменены"}


@router.delete("/{answer_id}")
async def delete_answer(answer_id: uuid.UUID, db: DBDep):
    await AnswersService(db).delete_answer(answer_id)
    return {"message": "Данные удалены"}
