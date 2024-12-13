import uuid
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, ForeignKey

from src.database import Base


# TODO: Модель вопроса
class QuestionOrm(Base):
    __tablename__ = "questions"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: Mapped[str | None] = mapped_column(
        String(999)
    )  # TODO: Заголовок или краткое описание вопросов
    description: Mapped[str | None] = mapped_column(String())  # TODO: Полное описание вопросов
    files: Mapped[list[str] | None] = mapped_column(
        ARRAY(String), nullable=True
    )  # TODO Вставка файлов
    ticket_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("tickets.id")
    )  # TODO: Связь с билетом
    theme_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("themes.id")
    )  # TODO: Связь с темой
