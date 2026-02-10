"""
Клиент для входа пользователя (POST /auth/token/login).

Отправляет LoginUserRequest (логин, пароль). Ответ — LoginUserResponse с токеном и данными пользователя.
Токен далее используется в auth_headers() для защищённых запросов.
"""

import requests
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.models.login_user_response import LoginUserResponse
from src.main.api.requests.requester import Requester


class LoginUserRequester(Requester):
    """POST /auth/token/login с телом login_user_request; возвращает LoginUserResponse с токеном и user."""

    def post(self, login_user_request: LoginUserRequest) -> LoginUserResponse:
        url = f'{self.base_url}/auth/token/login'
        response = requests.post(
            url=url,
            json=login_user_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        return LoginUserResponse(**response.json())
