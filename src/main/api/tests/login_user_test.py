"""
API-тесты входа (логина).

Проверяется вход под админом (роль ROLE_ADMIN) и под обычным пользователем (ROLE_USER),
созданным через /admin/create. Ожидается 200 и совпадение username/role в ответе.
"""

import pytest
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.requests.login_user_requster import LoginUserRequester
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.requests.create_user_requester import CreateUserRequester


@pytest.mark.api
class TestUserLogin:
    """Тесты эндпоинта логина (POST /auth/token/login)."""

    def test_login_admin(self):
        """Вход под admin/123456 — в ответе user.username и user.role == ROLE_ADMIN."""
        login_user_request = LoginUserRequest(username="admin", password="123456")

        response = LoginUserRequester(
            request_spec=RequestSpecs.unauthorized_headers(),
            response_spec=ResponseSpecs.code_200()
        ).post(login_user_request)

        assert login_user_request.username == response.user.username
        assert response.user.role == 'ROLE_ADMIN'

    def test_login_user(self):
        """Создаём пользователя Max33, логинимся — в ответе username и role ROLE_USER."""
        create_user_request = CreateUserRequest(username="Max33", password="Pas!sw0rd", role="ROLE_USER")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.code_200()
        ).post(create_user_request)

        login_user_request = LoginUserRequest(username="Max33", password="Pas!sw0rd")

        response = LoginUserRequester(
            request_spec=RequestSpecs.unauthorized_headers(),
            response_spec=ResponseSpecs.code_200()
        ).post(login_user_request)

        assert login_user_request.username == response.user.username
        assert response.user.role == 'ROLE_USER'
