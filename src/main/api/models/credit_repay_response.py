"""
Модель ответа API на погашение кредита.

Возвращается после успешного POST /credit/repay: id кредита и внесённая сумма.
"""

from src.main.api.models.base_model import BaseModel


class CreditRepayResponse(BaseModel):
    """Ответ: id кредита и сумма, зачисленная в погашение."""
    creditId: int
    amountDeposited: float
