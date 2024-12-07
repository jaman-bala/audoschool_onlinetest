import uuid
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class QuestionAddRequest(BaseModel):
    title: str = Field(default=None, max_length=999)
    description: str = Field(default=None)
    ticket_id: uuid.UUID
    theme_id: uuid.UUID


class QuestionAdd(BaseModel):
    title: str = Field(default=None, max_length=999)
    description: str = Field(default=None)
    ticket_id: uuid.UUID
    theme_id: uuid.UUID


class Question(BaseModel):
    id: uuid.UUID
    title: str = Field(default=None, max_length=999)
    description: str = Field(default=None)
    photo: str = Field(default=None)
    created_date: datetime
    updated_date: datetime

    model_config = ConfigDict(from_attributes=True)
