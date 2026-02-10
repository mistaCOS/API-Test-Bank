"""
Модель запроса на создание пользователя (админский эндпоинт).

Тело запроса для POST /admin/create: логин, пароль и роль пользователя.
"""

from src.main.api.models.base_model import BaseModel


class CreateUserRequest(BaseModel):
    """Запрос: имя пользователя, пароль и роль (например ROLE_USER, ROLE_ADMIN)."""
    username: str
    password: str
    role: str
