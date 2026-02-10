"""
Модель запроса на вход (логин).

Тело запроса для POST /auth/token/login: логин и пароль для получения токена.
"""

from src.main.api.models.base_model import BaseModel


class LoginUserRequest(BaseModel):
    """Запрос: имя пользователя и пароль."""
    username: str
    password: str
