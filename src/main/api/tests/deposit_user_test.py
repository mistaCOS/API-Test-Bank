"""
API-тесты пополнения счёта (депозит).

Проверяется успешное пополнение (баланс и id счёта в ответе) и ошибка 404
при пополнении несуществующего счёта.
"""

import pytest
from src.main.api.models.create_deposit_request import CreateDepositRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.requests.create_account_requester import CreateAccountRequester
from src.main.api.requests.create_deposit_requester import CreateDepositRequester
from src.main.api.requests.create_user_requester import CreateUserRequester
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs


@pytest.mark.api
class TestUserDeposit:
    """Тесты эндпоинта пополнения счёта (POST /account/deposit)."""

    def test_deposit_user(self):
        """Создаём пользователя и счёт, пополняем на 2000 — в ответе id счёта и баланс равны переданным."""
        create_user_request = CreateUserRequest(username="Max44", password="Pas!sw0rd", role="ROLE_USER")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.code_200()
        ).post(create_user_request)

        response = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="Max44", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.code_201()
        ).post()

        account_id = response.id
        create_deposit_request = CreateDepositRequest(accountId=account_id, amount=2000)

        response = CreateDepositRequester(
            request_spec=RequestSpecs.auth_headers(username="Max44", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.code_200()
        ).post(create_deposit_request)

        assert create_deposit_request.accountId == response.id
        assert create_deposit_request.amount == response.balance

    def test_deposit_user_with_bad_request(self):
        """Пополнение счёта с несуществующим accountId (1000) — ожидается 404."""
        create_user_request = CreateUserRequest(username="Max55", password="Pas!sw0rd", role="ROLE_USER")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.code_200()
        ).post(create_user_request)

        CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="Max55", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.code_201()
        ).post()

        create_deposit_request = CreateDepositRequest(accountId=1000, amount=2000)

        CreateDepositRequester(
            request_spec=RequestSpecs.auth_headers(username="Max55", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.code_404()
        ).post(create_deposit_request)
