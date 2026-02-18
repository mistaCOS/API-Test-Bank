import pytest
from src.main.api.models.create_credit_request import CreateCreditRequest


@pytest.mark.api
class TestUserCreditRequest:
    def test_user_credit_request(self, api_manager, create_user_secret_request, create_account_secret_response,
                                 get_credit_history):
        create_credit_request = CreateCreditRequest(accountId=create_account_secret_response.id, amount=5000,
                                                    termMonths=12)

        response = api_manager.user_steps.create_credit(create_user_secret_request, create_credit_request)

        assert create_credit_request.accountId == response.id
        assert create_credit_request.amount == response.amount
        assert create_credit_request.termMonths == response.termMonths

        history = api_manager.user_steps.get_credit_history(create_user_secret_request)
        credit = next((c for c in history.credits if c.creditId == response.creditId), None)
        assert credit is not None
        assert credit.amount == response.amount
        assert credit.termMonths == response.termMonths

    def test_user_credit_request_with_empty_amount(self, api_manager, create_user_secret_request,
                                                   create_account_secret_response):
        create_credit_request = CreateCreditRequest(accountId=create_account_secret_response.id, amount=0,
                                                    termMonths=12)

        api_manager.user_steps.create_credit_invalid(create_user_secret_request, create_credit_request)
