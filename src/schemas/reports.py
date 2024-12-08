import uuid
from pydantic import BaseModel, ConfigDict
from datetime import datetime, date


class ReportAddRequest(BaseModel):
    user_id: uuid.UUID
    ticket_id: uuid.UUID
    theme_id: uuid.UUID
    points: int | None = None
    date_from: date | None = None
    date_end: date | None = None


class ReportAdd(BaseModel):
    user_id: uuid.UUID
    ticket_id: uuid.UUID
    theme_id: uuid.UUID
    points: int | None = None
    date_from: date | None = None
    date_end: date | None = None
    created_date: datetime
    updated_date: datetime


class ReportPatch(BaseModel):
    user_id: uuid.UUID
    ticket_id: uuid.UUID
    theme_id: uuid.UUID
    points: int | None = None
    date_from: date | None = None
    date_end: date | None = None


class Report(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    ticket_id: uuid.UUID
    theme_id: uuid.UUID
    points: int | None = None
    date_from: date | None = None
    date_end: date | None = None
    created_date: datetime
    updated_date: datetime

    model_config = ConfigDict(from_attributes=True)
