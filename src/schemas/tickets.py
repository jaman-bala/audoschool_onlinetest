import uuid
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class TicketAddRequest(BaseModel):
    title: str | None = None


class TicketAdd(BaseModel):
    title: str | None = None
    created_date: datetime
    updated_date: datetime


class TicketPatch(BaseModel):
    title: str | None = None


class Ticket(BaseModel):
    id: uuid.UUID
    title: str | None = None
    created_date: datetime
    updated_date: datetime

    model_config = ConfigDict(from_attributes=True)
