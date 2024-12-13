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
    files: list[str] | None = None


class QuestionPatch(BaseModel):
    title: str
    description: str
    ticket_id: uuid.UUID
    theme_id: uuid.UUID


class QuestionPatchFile(BaseModel):
    files: list[str] | None = None


class Question(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    ticket_id: uuid.UUID
    theme_id: uuid.UUID
    files: list[str] | None = None

    model_config = ConfigDict(from_attributes=True)
