import pytest

from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.models.login_user_request import LoginUserRequest


@pytest.fixture
def get_users(api_manager):
    def _fetch():
        return api_manager.admin_steps.get_user(
            LoginUserRequest(username="admin", password="123456")
        )
    return _fetch


@pytest.fixture
def get_transactions(api_manager, create_user_request):
    def _fetch(account_id: int):
        return api_manager.user_steps.get_transactions(create_user_request, account_id)
    return _fetch


@pytest.fixture
def get_credit_history(api_manager, create_user_secret_request):
    def _fetch():
        return api_manager.user_steps.get_credit_history(create_user_secret_request)
    return _fetch

