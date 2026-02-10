"""
Модель ответа API на создание пользователя.

Возвращается после успешного POST /admin/create: данные созданного пользователя.
"""

from src.main.api.models.base_model import BaseModel


class CreateUserResponse(BaseModel):
    """Ответ: id, логин, пароль и роль созданного пользователя."""
    id: int
    username: str
    password: str
    role: str
