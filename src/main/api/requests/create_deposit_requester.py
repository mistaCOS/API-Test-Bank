"""
Клиент для пополнения счёта (POST /account/deposit).

Отправляет CreateDepositRequest (id счёта, сумма). При успехе возвращает CreateDepositResponse,
иначе — объект Response для проверки кода и тела ошибки.
"""
from http import HTTPStatus
from requests import Response
from src.main.api.models.create_deposit_request import CreateDepositRequest
from src.main.api.models.create_deposit_response import CreateDepositResponse
from src.main.api.requests.requester import Requester
import requests


class CreateDepositRequester(Requester):
    """POST /account/deposit с телом create_deposit_request; при 200 — возвращает CreateDepositResponse."""

    def post(self, create_deposit_request: CreateDepositRequest) -> CreateDepositResponse | Response:
        url = f'{self.base_url}/account/deposit'
        response = requests.post(
            url=url,
            json=create_deposit_request.model_dump(),
            headers=self.headers,
        )
        self.response_spec(response)
        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]:
            return CreateDepositResponse(**response.json())
        return response
