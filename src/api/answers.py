from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.services.answers import AnswersService
from src.schemas.answers import AnswerAddRequest

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
