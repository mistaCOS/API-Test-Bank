import pytest
from src.main.api.models.credit_repay_request import CreditRepayRequest


@pytest.mark.api
class TestUserCreditRepay:
    def test_user_credit_repay(self, api_manager, create_user_secret_request, create_credit_response,
                               get_credit_history):
        credit_repay_request = CreditRepayRequest(creditId=create_credit_response.creditId,
                                                  accountId=create_credit_response.id,
                                                  amount=create_credit_response.balance)

        response = api_manager.user_steps.create_credit_repay(create_user_secret_request, credit_repay_request)

        assert credit_repay_request.creditId == response.creditId
        assert credit_repay_request.amount == response.amountDeposited

        history = api_manager.user_steps.get_credit_history(create_user_secret_request)
        credit = next((c for c in history.credits if c.creditId == response.creditId), None)
        assert credit is not None
        assert credit.balance == 0

    def test_user_credit_repay_wrong_amount(self, api_manager, create_user_secret_request, create_credit_response):
        credit_repay_request = CreditRepayRequest(creditId=create_credit_response.creditId,
                                                  accountId=create_credit_response.id,
                                                  amount=1000)

        api_manager.user_steps.create_credit_repay_invalid(create_user_secret_request, credit_repay_request)
