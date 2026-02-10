"""
Клиент для создания счёта (POST /account/create).

Запрос без тела: счёт создаётся для текущего авторизованного пользователя.
Заголовки должны содержать Authorization (Bearer token).
"""

import requests

from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.requests.requester import Requester


class CreateAccountRequester(Requester):
    """Отправляет POST на /account/create, проверяет ответ через response_spec, возвращает CreateAccountResponse."""

    def post(self, model=None) -> CreateAccountResponse:
        url = f'{self.base_url}/account/create'
        response = requests.post(
            url=url,
            headers=self.headers,
        )
        self.response_spec(response)
        return CreateAccountResponse(**response.json())
