"""
Клиент для оформления кредита (POST /credit/request).

Отправляет CreateCreditRequest (счёт, сумма, срок), при успехе возвращает CreateCreditResponse.
При ошибке возвращает объект Response для анализа (например status_code, text).
"""

from http import HTTPStatus

from requests import Response
from src.main.api.models.create_credit_request import CreateCreditRequest
from src.main.api.models.create_credit_response import CreateCreditResponse
from src.main.api.requests.requester import Requester
import requests


class CreateCreditRequester(Requester):
    """POST /credit/request с телом create_credit_request; при 200/201 — парсит и возвращает CreateCreditResponse."""

    def post(self, create_credit_request: CreateCreditRequest) -> CreateCreditResponse | Response:
        url = f'{self.base_url}/credit/request'
        response = requests.post(
            url=url,
            json=create_credit_request.model_dump(),
            headers=self.headers,
        )
        self.response_spec(response)
        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]:
            return CreateCreditResponse(**response.json())
        return response
