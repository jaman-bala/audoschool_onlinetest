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
