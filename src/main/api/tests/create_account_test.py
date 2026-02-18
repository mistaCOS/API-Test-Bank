import pytest


@pytest.mark.api
class TestCreateAccount:
    def test_create_account(self, api_manager, create_user_request, get_transactions):
        response = api_manager.user_steps.create_account(create_user_request)

        assert response.balance == 0

        transactions_response = api_manager.user_steps.get_transactions(create_user_request,  response.id)
        assert response.id == transactions_response.id
        assert response.number == transactions_response.number
        assert transactions_response.balance == 0
