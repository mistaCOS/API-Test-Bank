import pytest
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.login_user_request import LoginUserRequest


@pytest.mark.api
class TestCreateUser:
    @pytest.mark.parametrize(
        'create_user_request',
        [RandomModelGenerator.generate(CreateUserRequest)]
    )
    def test_create_user_valid(self, api_manager, create_user_request, get_users):
        response = api_manager.admin_steps.create_user(create_user_request)

        assert create_user_request.username == response.username
        assert create_user_request.role == response.role

        users = api_manager.admin_steps.get_user(
            LoginUserRequest(username="admin", password="123456")
        )
        assert any(u.username == create_user_request.username for u in users.root)

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
    def test_create_user_invalid(self, username, password, api_manager):
        create_user_request = CreateUserRequest(username=username, password=password, role="ROLE_USER")
        api_manager.admin_steps.create_invalid_user(create_user_request)
