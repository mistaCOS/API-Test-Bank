import requests
import pytest

from src.main.api.models.create_credit_request import CreateCreditRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.requests.create_account_requester import CreateAccountRequester
from src.main.api.requests.create_credit_requester import CreateCreditRequester
from src.main.api.requests.create_user_requester import CreateUserRequester
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs


@pytest.mark.api
class TestUserCreditRequest:
    def test_user_credit_request(self):
        create_user_request = CreateUserRequest(username="Max77", password="Pas!sw0rd", role="ROLE_CREDIT_SECRET")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.code_200()
        ).post(create_user_request)

        response = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="Max77", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.code_201()
        ).post()

        account_id = response.id

        create_credit_request = CreateCreditRequest(accountId=account_id, amount=5000, termMonths=12)

        response = CreateCreditRequester(
            request_spec=RequestSpecs.auth_headers(username="Max77", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.code_201()
        ).post(create_credit_request)

        assert create_credit_request.accountId == response.id
        assert create_credit_request.amount == response.amount
        assert create_credit_request.termMonths == response.termMonths
