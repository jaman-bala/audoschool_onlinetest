from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.schemas.questions import QuestionAddRequest
from src.services.questions import QuestionsService

router = APIRouter(prefix="/questions", tags=["Вопросы"])


@router.post("/create", summary="Создание билетов")
async def create_question(
    data: QuestionAddRequest,
    db: DBDep,
):
    new_question = await QuestionsService(db).create_questions(data)
    return {
        "message": "Вопрос создан",
        "question_id": new_question.id,
    }
