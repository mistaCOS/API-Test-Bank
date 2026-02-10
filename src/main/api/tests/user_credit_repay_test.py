"""
API-тесты погашения кредита (POST /credit/repay).

Проверяется успешное погашение кредита полной суммой (совпадение creditId и amountDeposited)
и ошибка 422 при попытке погасить неверную сумму (например 100 вместо полного остатка).
"""

import pytest
from src.main.api.models.create_credit_request import CreateCreditRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.requests.create_account_requester import CreateAccountRequester
from src.main.api.requests.create_credit_requester import CreateCreditRequester
from src.main.api.requests.create_user_requester import CreateUserRequester
from src.main.api.requests.credit_repay_requester import CreditRepayRequester
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs


@pytest.mark.api
class TestUserCreditRepay:
    """Тесты эндпоинта погашения кредита."""

    def test_user_credit_repay(self):
        """Пользователь с ролью ROLE_CREDIT_SECRET: создаём счёт, оформляем кредит, погашаем полной суммой — проверяем creditId и amountDeposited."""
        create_user_request = CreateUserRequest(username="Max88", password="Pas!sw0rd", role="ROLE_CREDIT_SECRET")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.code_200()
        ).post(create_user_request)

        response = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="Max88", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.code_201()
        ).post()

        create_credit_request = CreateCreditRequest(accountId=response.id, amount=5000, termMonths=12)

        response = CreateCreditRequester(
            request_spec=RequestSpecs.auth_headers(username="Max88", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.code_201()
        ).post(create_credit_request)

        credit_repay_request = CreditRepayRequest(creditId=response.creditId, accountId=response.id,
                                                  amount=response.balance)

        response = CreditRepayRequester(
            request_spec=RequestSpecs.auth_headers(username="Max88", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.code_200()
        ).post(credit_repay_request)

        assert credit_repay_request.creditId == response.creditId
        assert credit_repay_request.amount == response.amountDeposited

    def test_user_credit_repay_wrong_amount(self):
        """Погашение с суммой 100 вместо полного остатка — ожидается 422."""
        create_user_request = CreateUserRequest(username="Max88", password="Pas!sw0rd", role="ROLE_CREDIT_SECRET")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.code_200()
        ).post(create_user_request)

        response = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="Max88", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.code_201()
        ).post()

        create_credit_request = CreateCreditRequest(accountId=response.id, amount=5000, termMonths=12)

        response = CreateCreditRequester(
            request_spec=RequestSpecs.auth_headers(username="Max88", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.code_201()
        ).post(create_credit_request)

        credit_repay_request = CreditRepayRequest(creditId=response.creditId, accountId=response.id,
                                                  amount=100)

        CreditRepayRequester(
            request_spec=RequestSpecs.auth_headers(username="Max88", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.code_422()
        ).post(credit_repay_request)
