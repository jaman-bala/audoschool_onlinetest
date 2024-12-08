import uuid
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class ThemeAddRequest(BaseModel):
    title: str | None = None


class ThemeAdd(BaseModel):
    title: str | None = None
    created_date: datetime
    updated_date: datetime


class ThemePatch(BaseModel):
    title: str | None = None


class Theme(BaseModel):
    id: uuid.UUID
    title: str | None = None
    created_date: datetime
    updated_date: datetime

    model_config = ConfigDict(from_attributes=True)
