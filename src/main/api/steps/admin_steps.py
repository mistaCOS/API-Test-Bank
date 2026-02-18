from src.main.api.foundation.endpoint import EndPoint
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester


class AdminSteps(BaseSteps):
    def create_user(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username="admin", password="123456"),
            EndPoint.ADMIN_CREATE_USER,
            ResponseSpecs.code_200()
        ).post(create_user_request)

        self.created_obj.append(response)
        return response

    def delete_user(self, user_id: int):
        CrudRequester(
            RequestSpecs.auth_headers(username="admin", password="123456"),
            EndPoint.ADMIN_DELETE_USER,
            ResponseSpecs.code_200()
        ).delete(user_id)

    def create_invalid_user(self, create_user_request: CreateUserRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username="admin", password="123456"),
            EndPoint.ADMIN_CREATE_USER,
            ResponseSpecs.code_400()
        ).post(create_user_request)

    def login_user(self, login_user_request: LoginUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.unauthorized_headers(),
            EndPoint.LOGIN_USER,
            ResponseSpecs.code_200()
        ).post(login_user_request)
        return response

    def get_user(self, login_user_request: LoginUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username="admin", password="123456"),
            EndPoint.GET_USER,
            ResponseSpecs.code_200()
        ).get()
        return response