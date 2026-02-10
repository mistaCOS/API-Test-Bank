"""
Клиент для погашения кредита (POST /credit/repay).

Отправляет CreditRepayRequest (id кредита, id счёта, сумма погашения).
При успехе (200/201) возвращает CreditRepayResponse, иначе — Response.
"""

from http import HTTPStatus
import requests
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_repay_response import CreditRepayResponse
from src.main.api.requests.requester import Requester
from requests import Response


class CreditRepayRequester(Requester):
    """POST /credit/repay с телом credit_repay_request; при 200/201 — возвращает CreditRepayResponse."""

    def post(self, credit_repay_request: CreditRepayRequest) -> CreditRepayResponse | Response:
        url = f'{self.base_url}/credit/repay'
        response = requests.post(
            url=url,
            json=credit_repay_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]:
            return CreditRepayResponse(**response.json())
        return response
