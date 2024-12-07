import uuid
from pydantic import BaseModel, ConfigDict
from datetime import datetime, date

class PaymentAddRequest(BaseModel):
    user_id: uuid.UUID
    date_ckeck: date
    price: int

class PaymentAdd(BaseModel):
    user_id: uuid.UUID
    date_ckeck: date
    price: int

class PaymentPatch(BaseModel):
    user_id: uuid.UUID
    date_ckeck: date
    price: int

class Payment(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    date_ckeck: date
    price: int
    created_date: datetime
    updated_date: datetime

    model_config = ConfigDict(from_attributes=True)