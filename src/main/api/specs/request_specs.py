"""
Спецификации для формирования запросов к API.

Содержит методы для получения заголовков: базовые (JSON), с авторизацией (логин → токен)
и без авторизации. Используются всеми реквестами при инициализации Requester.
"""

import requests
from src.main.api.configs.config import Config
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.models.login_user_response import LoginUserResponse


class RequestSpecs:
    """Статические методы для сборки request_spec (headers + base_url) для Requester."""

    @staticmethod
    def base_headers():
        """Заголовки для JSON-запросов без авторизации."""
        return {
            "Content-Type": "application/json",
            "accept": "application/json"
        }

    @staticmethod
    def auth_headers(username: str, password: str):
        """
        Выполняет логин по username/password, получает токен и возвращает request_spec
        с заголовком Authorization: Bearer <token> и base_url из Config.
        При неудачном логине выбрасывает Exception.
        """
        request = LoginUserRequest(username=username, password=password)
        response = requests.post(
            url='http://localhost:4111/api/auth/token/login',
            json=request.model_dump(),
            headers=RequestSpecs.base_headers()
        )
        if response.status_code == 200:
            response_data = LoginUserResponse(**response.json())
            token = response_data.token
            headers = RequestSpecs.base_headers()
            headers["Authorization"] = f"Bearer {token}"
            return {
                "headers": headers,
                "base_url": Config.fetch('backendUrl')
            }
        raise Exception("Login failed")

    @staticmethod
    def unauthorized_headers():
        """Заголовки без токена; base_url из Config. Для логина и публичных эндпоинтов."""
        return {
            "headers": RequestSpecs.base_headers(),
            "base_url": Config.fetch('backendUrl')
        }
