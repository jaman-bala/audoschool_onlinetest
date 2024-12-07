import uuid
from typing import Optional
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import DateTime, ForeignKey, Integer, Date
from datetime import datetime, date

from src.database import Base


class ReportOrm(Base):
    __tablename__ = "reports"

    id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"))
    ticket_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("tickets.id"))
    theme_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("themes.id"))
    points: Mapped[Optional[int]] = mapped_column(Integer)
    date_from: Mapped[Optional[date]] = mapped_column(Date)
    date_end: Mapped[Optional[date]] = mapped_column(Date)

    created_date: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )  # TODO: Дата создание
    updated_date: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), onupdate=func.now()
    )  # TODO: Дата обновление
