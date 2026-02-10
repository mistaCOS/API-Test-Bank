"""
Модель запроса на погашение кредита.

Тело запроса для POST /credit/repay: id кредита, id счёта для списания и сумма погашения.
"""

from src.main.api.models.base_model import BaseModel


class CreditRepayRequest(BaseModel):
    """Запрос: id кредита, id счёта, сумма погашения."""
    creditId: int
    accountId: int
    amount: float
