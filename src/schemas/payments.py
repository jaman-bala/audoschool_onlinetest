import uuid
from pydantic import BaseModel, ConfigDict
from datetime import datetime, date


class PaymentAddRequest(BaseModel):
    user_id: uuid.UUID
    date_check: date
    price: int


class PaymentAdd(BaseModel):
    user_id: uuid.UUID
    date_check: date
    price: int
    created_date: datetime
    updated_date: datetime


class PaymentPatch(BaseModel):
    user_id: uuid.UUID
    date_check: date
    price: int


class Payment(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    date_check: date
    price: int
    created_date: datetime
    updated_date: datetime

    model_config = ConfigDict(from_attributes=True)
