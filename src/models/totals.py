import uuid
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, ForeignKey, Integer, Date
from sqlalchemy.sql import func
from datetime import datetime, date

from src.database import Base


# TODO: Модель финальный экзамен
class TotalOrm(Base):
    __tablename__ = "totals"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"))
    points: Mapped[int | None] = mapped_column(Integer)
    date_from: Mapped[date | None] = mapped_column(Date)
    date_end: Mapped[date | None] = mapped_column(Date)

    created_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )  # TODO: Дата создания записи
    updated_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), onupdate=func.now()
    )  # TODO: Дата обновления записи

    @hybrid_property
    def duration_in_days(self):
        """Вычисляет длительность обучения в днях."""
        if self.date_from and self.date_end:
            return (self.date_end - self.date_from).days
        return None

    @hybrid_property
    def is_valid_date_range(self):
        """Проверяет, что дата окончания позже или равна дате начала."""
        if self.date_from and self.date_end:
            return self.date_end >= self.date_from
        return False
