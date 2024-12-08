import uuid
import typing
from typing import Optional
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from sqlalchemy import String, DateTime, ForeignKey

from src.database import Base

if typing.TYPE_CHECKING:
    from src.models import QuestionOrm


class AvatarOrm(Base):
    __tablename__ = "avatars"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"))
    image_path: Mapped[str | None] = mapped_column(String(200))

    created_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )  # TODO: Дата создание
    updated_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), onupdate=func.now()
    )  # TODO: Дата обновление


class ImagesOrm(Base):
    __tablename__ = "images"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    path: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    created_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )  # TODO: Дата создание
    updated_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), onupdate=func.now()
    )  # TODO: Дата обновление

    questions: Mapped[list["QuestionOrm"]] = relationship(
        "QuestionOrm", back_populates="images", secondary="questions_images"
    )


class QuestionsImagesOrm(Base):
    __tablename__ = "questions_images"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("questions.id"))
    image_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("images.id"))
