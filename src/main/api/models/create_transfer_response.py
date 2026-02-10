"""
Модель ответа API на перевод между счетами.

Возвращается после успешного POST /account/transfer: счета и баланс счёта отправителя.
"""

from src.main.api.models.base_model import BaseModel


class CreateTransferResponse(BaseModel):
    """Ответ: id обоих счетов и баланс счёта отправителя после перевода."""
    fromAccountId: int
    toAccountId: int
    fromAccountIdBalance: float
