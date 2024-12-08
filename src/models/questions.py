import uuid
import typing
from typing import Optional
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, DateTime, ForeignKey
from datetime import datetime

from src.database import Base

if typing.TYPE_CHECKING:
    from src.models import ImagesOrm


# TODO: Модель вопроса
class QuestionOrm(Base):
    __tablename__ = "questions"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: Mapped[Optional[str]] = mapped_column(
        String(999)
    )  # TODO: Заголовок или краткое описание вопросов
    description: Mapped[Optional[str]] = mapped_column(String())  # TODO: Полное описание вопросов
    photo: Mapped[Optional[str]] = mapped_column(
        String(999)
    )  # TODO: Путь или URL к изображению вопроса
    ticket_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("tickets.id")
    )  # TODO: Связь с билетом
    theme_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("themes.id")
    )  # TODO: Связь с темой

    created_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )  # TODO: Дата создание
    updated_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), onupdate=func.now()
    )  # TODO: Дата обновление

    images: Mapped[list["ImagesOrm"]] = relationship(
        "ImagesOrm", back_populates="questions", secondary="questions_images"
    )
