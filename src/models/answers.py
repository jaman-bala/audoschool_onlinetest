import uuid
from typing import Optional
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.sql import func
from datetime import datetime

from src.database import Base


# TODO: Модель ответа
class AnswerOrm(Base):
    __tablename__ = "answers"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: Mapped[Optional[str]] = mapped_column(String(999))  # TODO: Текст ответа
    is_correct: Mapped[Optional[bool]] = mapped_column(Boolean, default=False)
    question_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("questions.id")
    )  # TODO: Связь с вопросом

    created_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )  # TODO: Дата создание
    updated_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), onupdate=func.now()
    )  # TODO: Дата обновление
