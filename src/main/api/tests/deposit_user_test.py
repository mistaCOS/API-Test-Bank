import pytest
from src.main.api.models.create_deposit_request import CreateDepositRequest


@pytest.mark.api
class TestUserDeposit:
    def test_deposit_user(self, api_manager, create_user_request, create_account_response, get_transactions):
        create_deposit_request = CreateDepositRequest(accountId=create_account_response.id, amount=2000)

        response = api_manager.user_steps.create_deposit(create_user_request, create_deposit_request)

        assert create_deposit_request.accountId == response.id
        assert create_deposit_request.amount == response.balance

        transactions_response = api_manager.user_steps.get_transactions(create_user_request,  response.id)
        assert transactions_response.id == response.id
        assert transactions_response.balance == response.balance

    def test_deposit_user_with_bad_request(self, api_manager, create_user_request):

        create_deposit_request = CreateDepositRequest(accountId=1000, amount=2000)

        api_manager.user_steps.create_deposit_invalid(create_user_request, create_deposit_request)
