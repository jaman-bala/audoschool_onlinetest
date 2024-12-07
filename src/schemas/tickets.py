from typing import List
from uuid import UUID
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class TicketAddRequest(BaseModel):
    title: str | None = None
    description: str | None = None


class TicketAdd(BaseModel):
    title: str | None = None
    description: str | None = None
    created_date: datetime
    updated_date: datetime


class TicketUpdate(BaseModel):
    title: str | None = None
    description: str | None = None


class Ticket(BaseModel):
    id: UUID
    title: str | None = None
    description: str | None = None
    created_date: datetime
    updated_date: datetime

    model_config = ConfigDict(from_attributes=True)


class TicketWithQuestions(Ticket):
    questions: List[UUID]


class TicketDetailedResponse(TicketWithQuestions):
    exams: List[UUID]
