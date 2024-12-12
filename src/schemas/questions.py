import uuid
from pydantic import BaseModel, ConfigDict, Field


class QuestionAddRequest(BaseModel):
    title: str = Field(default=None, max_length=999)
    description: str = Field(default=None)
    ticket_id: uuid.UUID
    theme_id: uuid.UUID


class QuestionAdd(BaseModel):
    title: str
    description: str
    ticket_id: uuid.UUID
    theme_id: uuid.UUID
    files: list[str]


class QuestionPatch(BaseModel):
    title: str
    description: str
    ticket_id: uuid.UUID
    theme_id: uuid.UUID


class QuestionPatchFile(BaseModel):
    files: list[str]


class Question(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    ticket_id: uuid.UUID
    theme_id: uuid.UUID
    files: list[str]

    model_config = ConfigDict(from_attributes=True)
