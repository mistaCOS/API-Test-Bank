"""
Модель ответа API на оформление кредита.

Возвращается после успешного POST /credit/request: данные по выданному кредиту.
"""

from src.main.api.models.base_model import BaseModel


class CreateCreditResponse(BaseModel):
    """Ответ: id записи, сумма, срок, остаток долга и id кредита."""
    id: int
    amount: float
    termMonths: int
    balance: float
    creditId: int
