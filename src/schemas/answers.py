import uuid
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class AnswerAddRequest(BaseModel):
    title: str | None = None
    is_correct: bool = False
    question_id: uuid.UUID


class AnswerAdd(BaseModel):
    title: str | None = None
    is_correct: bool = False
    question_id: uuid.UUID
    created_date: datetime
    updated_date: datetime


class AnswerPatch(BaseModel):
    title: str | None = None
    is_correct: bool = False
    question_id: uuid.UUID


class Answer(BaseModel):
    id: uuid.UUID
    title: str | None = None
    is_correct: bool = False
    question_id: uuid.UUID
    created_date: datetime
    updated_date: datetime

    model_config = ConfigDict(from_attributes=True)
