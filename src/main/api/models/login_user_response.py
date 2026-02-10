"""
Модель ответа API на логин.

Возвращается после успешного POST /auth/token/login: токен доступа и данные пользователя.
Токен передаётся в заголовке Authorization для защищённых эндпоинтов.
"""

from src.main.api.models.base_model import BaseModel


class User(BaseModel):
    """Краткие данные пользователя: логин и роль."""
    username: str
    role: str


class LoginUserResponse(BaseModel):
    """Ответ: JWT-токен и объект пользователя (username, role)."""
    token: str
    user: User
