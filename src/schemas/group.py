import uuid
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class GroupAddRequest(BaseModel):
    title: str | None = None
    category: str | None = None
    user_quantity: int | None = None
    date_from: datetime | None = None
    date_end: datetime | None = None
    period: str | None = None


class GroupAdd(BaseModel):
    title: str | None = None
    category: str | None = None
    user_quantity: int | None = None
    date_from: datetime | None = None
    date_end: datetime | None = None
    period: str | None = None
    is_active: bool | None = True
    created_date: datetime | None = None
    updated_date: datetime | None = None


class GroupPatch(BaseModel):
    title: str | None = None
    category: str | None = None
    user_quantity: int | None = None
    date_from: datetime | None = None
    date_end: datetime | None = None
    period: str | None = None
    is_active: bool | None = None


class Group(BaseModel):
    id: uuid.UUID
    title: str | None = None
    category: str | None = None
    user_quantity: int | None = None
    date_from: datetime | None = None
    date_end: datetime | None = None
    period: str | None = None
    is_active: bool | None = None
    created_date: datetime | None = None
    updated_date: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
