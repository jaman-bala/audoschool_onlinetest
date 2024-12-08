from src.models.payments import PaymentOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import PaymentDataMapper


class PaymentsRepository(BaseRepository):
    model = PaymentOrm
    mapper = PaymentDataMapper
