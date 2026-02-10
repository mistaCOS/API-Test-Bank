"""
Клиент для создания пользователя (POST /admin/create).

Эндпоинт для администратора: отправляет CreateUserRequest (логин, пароль, роль).
При успехе (200/201) возвращает CreateUserResponse, иначе — Response.
"""

from http import HTTPStatus

from requests import Response

from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_response import CreateUserResponse
from src.main.api.requests.requester import Requester
import requests


class CreateUserRequester(Requester):
    """POST /admin/create с телом create_user_request; при 200/201 — возвращает CreateUserResponse."""

    def post(self, create_user_request: CreateUserRequest) -> CreateUserResponse | Response:
        url = f'{self.base_url}/admin/create'
        response = requests.post(
            url=url,
            json=create_user_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]:
            return CreateUserResponse(**response.json())
        return response
