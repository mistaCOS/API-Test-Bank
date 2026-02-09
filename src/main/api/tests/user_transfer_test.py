import pytest
from src.main.api.models.create_deposit_request import CreateDepositRequest
from src.main.api.models.create_transfer_request import CreateTransferRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.requests.create_account_requester import CreateAccountRequester
from src.main.api.requests.create_deposit_requester import CreateDepositRequester
from src.main.api.requests.create_transfer_requester import CreateTransferRequester
from src.main.api.requests.create_user_requester import CreateUserRequester
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs


@pytest.mark.api
class TestUserTransfer:
    def test_user_transfer(self):
        create_user_request = CreateUserRequest(username="Max55", password="Pas!sw0rd", role="ROLE_USER")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.code_200()
        ).post(create_user_request)

        response = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="Max55", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.code_201()
        ).post()

        from_account_id = response.id

        response = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="Max55", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.code_201()
        ).post()

        to_account_id = response.id

        create_deposit_request = CreateDepositRequest(accountId=from_account_id, amount=4000)

        response = CreateDepositRequester(
            request_spec=RequestSpecs.auth_headers(username="Max55", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.code_200()
        ).post(create_deposit_request)

        balance = response.balance

        create_transfer_request = CreateTransferRequest(fromAccountId=from_account_id, toAccountId=to_account_id,
                                                        amount=2000)

        response = CreateTransferRequester(
            request_spec=RequestSpecs.auth_headers(username="Max55", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.code_200()
        ).post(create_transfer_request)

        assert create_transfer_request.fromAccountId == response.fromAccountId
        assert create_transfer_request.toAccountId == response.toAccountId
        assert response.fromAccountIdBalance == balance - create_transfer_request.amount

    def test_user_transfer_invalid_account(self):
        create_user_request = CreateUserRequest(username="Max55", password="Pas!sw0rd", role="ROLE_USER")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.code_200()
        ).post(create_user_request)

        response = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="Max55", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.code_201()
        ).post()

        from_account_id = response.id

        CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="Max55", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.code_201()
        ).post()

        create_deposit_request = CreateDepositRequest(accountId=from_account_id, amount=4000)

        CreateDepositRequester(
            request_spec=RequestSpecs.auth_headers(username="Max55", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.code_200()
        ).post(create_deposit_request)

        create_transfer_request = CreateTransferRequest(fromAccountId=from_account_id, toAccountId=1000, amount=2000)

        CreateTransferRequester(
            request_spec=RequestSpecs.auth_headers(username="Max55", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.code_404()
        ).post(create_transfer_request)
