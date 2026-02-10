"""
API-тесты создания пользователя (POST /admin/create).

Проверяется успешное создание с валидными данными и ожидаемая ошибка 400
при невалидных логине/пароле (кириллица, короткий логин, неверный формат пароля и т.д.).
"""

import pytest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.requests.create_user_requester import CreateUserRequester
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs


@pytest.mark.api
class TestCreateUser:
    """Тесты эндпоинта создания пользователя администратором."""

    def test_create_user_valid(self):
        """Валидные username/password/role — пользователь создаётся, в ответе совпадают username и role."""
        create_user_request = CreateUserRequest(username="Max1", password="Pas!sw0rd", role="ROLE_USER")

        response = CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.code_200()
        ).post(create_user_request)

        assert create_user_request.username == response.username
        assert create_user_request.role == response.role

    @pytest.mark.parametrize(
        "username,password",
        [
            ("абв", "Pas!sw0rd"),
            ("ab", "Pas!sw0rd"),
            ("abc!", "Pas!sw0rd"),
            ("Max2", "Pas!sw0rд"),
            ("Max3", "Pas!sw0"),
            ("Max4", "pas!sw0rd"),
            ("Max5", "PAS!SW0RD"),
            ("Max6", "Pas!sword"),
        ]
    )
    def test_create_user_invalid(self, username, password):
        """Разные невалидные пары логин/пароль — API должен вернуть 400."""
        create_user_request = CreateUserRequest(username=username, password=password, role="ROLE_USER")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.code_400()
        ).post(create_user_request)
