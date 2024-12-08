from src.schemas.payments import PaymentAddRequest, PaymentAdd
from src.services.base import BaseService


class PaymentsService(BaseService):
    async def create_payments(self, data: PaymentAddRequest):
        new_payments = PaymentAdd(
            user_id=data.user_id,
            date_check=data.date_check,
            price=data.price,
        )
        await self.db.payments.add(new_payments)
        await self.db.commit()

    async def get_payments(self):
        await self.db.payments.get_all()
