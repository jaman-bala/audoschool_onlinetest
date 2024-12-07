import uuid
from typing import Optional
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, DateTime, Integer, String, Date
from sqlalchemy.sql import func
from datetime import datetime, date


from src.database import Base


# TODO: Модель Группы
class GroupOrm(Base):
    __tablename__ = "groups"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: Mapped[Optional[str]] = mapped_column(String(599))
    category: Mapped[Optional[str]] = mapped_column(String(599))
    user_quantity: Mapped[Optional[int]] = mapped_column(Integer, default=0)
    date_from: Mapped[date] = mapped_column(Date)
    date_end: Mapped[date] = mapped_column(Date)
    period: Mapped[Optional[str]] = mapped_column(String())  # TODO период обучения
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)  # TODO: Активность группы

    created_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )  # TODO: Дата создание
    updated_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), onupdate=func.now()
    )  # TODO: Дата обновление

    users = relationship("UsersOrm", back_populates="group")
