import uuid
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from datetime import datetime

from src.database import Base


# TODO: Модель билета
class TicketOrm(Base):
    __tablename__ = "tickets"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: Mapped[Optional[str]] = mapped_column(String(999))  # TODO: Название билета

    created_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )  # TODO: Дата создание
    updated_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), onupdate=func.now()
    )  # TODO: Дата обновление
