"""
Модель запроса на перевод между счетами.

Тело запроса для POST /account/transfer: счёт-источник, счёт-получатель и сумма.
"""

from src.main.api.models.base_model import BaseModel


class CreateTransferRequest(BaseModel):
    """Запрос: id счёта отправителя, id счёта получателя, сумма перевода."""
    fromAccountId: int
    toAccountId: int
    amount: float
