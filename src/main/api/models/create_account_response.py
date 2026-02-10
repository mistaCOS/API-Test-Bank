"""
Модель ответа API на создание счёта (account).

Используется при вызове POST /account/create — возвращает id счёта, номер и начальный баланс.
"""

from src.main.api.models.base_model import BaseModel


class CreateAccountResponse(BaseModel):
    """Ответ: созданный счёт — id, номер счёта и баланс (обычно 0)."""
    id: int
    number: str
    balance: float
