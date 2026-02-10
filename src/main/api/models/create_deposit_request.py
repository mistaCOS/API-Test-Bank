"""
Модель запроса на пополнение счёта (депозит).

Тело запроса для POST /account/deposit: id счёта и сумма пополнения.
"""

from src.main.api.models.base_model import BaseModel


class CreateDepositRequest(BaseModel):
    """Запрос: id счёта и сумма для зачисления."""
    accountId: int
    amount: float
