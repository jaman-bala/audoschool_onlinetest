import uuid
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, date
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from sqlalchemy import DateTime, ForeignKey, Integer, Date

from src.database import Base


# TODO: Модель платежа
class PaymentOrm(Base):
    __tablename__ = "payments"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"))
    date_check: Mapped[date] = mapped_column(Date)
    price: Mapped[int | None] = mapped_column(Integer, default=0)

    created_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )  # TODO: Дата создание
    updated_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), onupdate=func.now()
    )  # TODO: Дата обновление
