"""
Модель ответа API на пополнение счёта.

Возвращается после успешного POST /account/deposit: id счёта и новый баланс.
"""

from src.main.api.models.base_model import BaseModel


class CreateDepositResponse(BaseModel):
    """Ответ: id счёта и баланс после пополнения."""
    id: int
    balance: float
