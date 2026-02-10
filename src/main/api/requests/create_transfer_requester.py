"""
Клиент для перевода между счетами (POST /account/transfer).

Отправляет CreateTransferRequest (счёт отправителя, счёт получателя, сумма).
При успехе возвращает CreateTransferResponse, иначе — Response для анализа ошибки.
"""
from http import HTTPStatus
from requests import Response
from src.main.api.models.create_transfer_request import CreateTransferRequest
from src.main.api.models.create_transfer_response import CreateTransferResponse
from src.main.api.requests.requester import Requester
import requests


class CreateTransferRequester(Requester):
    """POST /account/transfer с телом create_transfer_request; при 200 — возвращает CreateTransferResponse."""

    def post(self, create_transfer_request: CreateTransferRequest) -> CreateTransferResponse | Response:
        url = f'{self.base_url}/account/transfer'
        response = requests.post(
            url=url,
            json=create_transfer_request.model_dump(),
            headers=self.headers,
        )
        self.response_spec(response)
        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]:
            return CreateTransferResponse(**response.json())
        return response
