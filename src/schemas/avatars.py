import uuid

from pydantic import BaseModel, ConfigDict
from datetime import datetime


class AvatarRequestAdd(BaseModel):
    filename: str | None = None
    file_path: str | None = None


class AvatarAdd(BaseModel):
    id: int
    file_path: str | None = None


class Avatar(BaseModel):
    id: int
    file_path: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class ImagesAddRequest(BaseModel):
    path: str | None = None


class ImagesAdd(BaseModel):
    path: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None


class ImagesPatch(BaseModel):
    path: str | None = None


class Images(BaseModel):
    id: uuid.UUID
    path: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class QuestionsImagesAdd(BaseModel):
    question_id: uuid.UUID
    image_id: uuid.UUID


class QuestionsImages(BaseModel):
    id: uuid.UUID
    question_id: uuid.UUID
    image_id: uuid.UUID

    model_config = ConfigDict(from_attributes=True)
