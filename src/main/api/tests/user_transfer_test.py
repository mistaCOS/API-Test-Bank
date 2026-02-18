import pytest
from src.main.api.models.create_transfer_request import CreateTransferRequest


@pytest.mark.api
class TestUserTransfer:
    def test_user_transfer(self, api_manager, create_user_request, create_account_response,
                           create_second_account_response, create_deposit_response, get_transactions):
        create_transfer_request = CreateTransferRequest(fromAccountId=create_account_response.id,
                                                        toAccountId=create_second_account_response.id,
                                                        amount=2000)
        response = api_manager.user_steps.create_transfer(create_user_request, create_transfer_request)

        assert create_transfer_request.fromAccountId == response.fromAccountId
        assert create_transfer_request.toAccountId == response.toAccountId

        transactions_response = get_transactions(create_account_response.id)
        assert transactions_response.balance == response.fromAccountIdBalance

    def test_user_transfer_invalid_account(self, api_manager, create_user_request, create_account_response,
                                           create_deposit_response):
        create_transfer_request = CreateTransferRequest(fromAccountId=create_account_response.id, toAccountId=1000,
                                                        amount=2000)
        api_manager.user_steps.create_transfer_invalid(create_user_request, create_transfer_request)
