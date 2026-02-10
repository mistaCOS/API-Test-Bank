"""
Модель запроса на оформление кредита.

Тело запроса для POST /credit/request: счёт, сумма кредита и срок в месяцах.
"""

from src.main.api.models.base_model import BaseModel


class CreateCreditRequest(BaseModel):
    """Запрос: id счёта, сумма кредита, срок в месяцах."""
    accountId: int
    amount: float
    termMonths: int
