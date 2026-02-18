import pytest

from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_credit_request import CreateCreditRequest
from src.main.api.models.create_deposit_request import CreateDepositRequest
from src.main.api.models.create_deposit_response import CreateDepositResponse
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_secret_request import CreateUserSecretRequest


@pytest.fixture
def create_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request


@pytest.fixture
def create_user_secret_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserSecretRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request


@pytest.fixture
def create_account_response(api_manager, create_user_request):
    return api_manager.user_steps.create_account(create_user_request)


@pytest.fixture
def create_second_account_response(api_manager, create_user_request):
    return api_manager.user_steps.create_account(create_user_request)


@pytest.fixture
def create_deposit_response(api_manager, create_user_request, create_account_response):
    deposit_request = CreateDepositRequest(accountId=create_account_response.id, amount=4000)
    return api_manager.user_steps.create_deposit(create_user_request, deposit_request)


@pytest.fixture
def create_account_secret_response(api_manager, create_user_secret_request):
    return api_manager.user_steps.create_account(create_user_secret_request)


@pytest.fixture
def create_credit_response(api_manager, create_account_secret_response, create_user_secret_request):
    credit_response = CreateCreditRequest(accountId=create_account_secret_response.id, amount=5000, termMonths=12)
    return api_manager.user_steps.create_credit(create_user_secret_request, credit_response)


