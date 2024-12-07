from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class AnswerAddRequest(BaseModel):
    text: str | None = None
    is_correct: bool = False


class AnswerAdd(BaseModel):
    text: str | None = None
    is_correct: bool = False
    question_id: UUID
    created_date: datetime
    updated_date: datetime


class Answer(BaseModel):
    id: UUID
    text: str | None = None
    is_correct: bool = False
    question_id: UUID
    created_date: datetime
    updated_date: datetime

    model_config = ConfigDict(from_attributes=True)
