from src.main.api.foundation.endpoint import EndPoint
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.create_credit_request import CreateCreditRequest
from src.main.api.models.create_deposit_request import CreateDepositRequest
from src.main.api.models.create_transfer_request import CreateTransferRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.get_credit_history_response import GetCreditHistoryResponse
from src.main.api.models.get_transactions_response import GetTransactionsResponse
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps
from src.main.api.foundation.requesters.crud_requester import CrudRequester


class UserSteps(BaseSteps):
    def create_account(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            EndPoint.CREATE_ACCOUNT,
            ResponseSpecs.code_201()
        ).post()
        return response

    def create_deposit(self, create_user_request: CreateUserRequest, create_deposit_request: CreateDepositRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            EndPoint.CREATE_DEPOSIT,
            ResponseSpecs.code_200()
        ).post(create_deposit_request)
        return response

    def create_deposit_invalid(self, create_user_request: CreateUserRequest,
                               create_deposit_request: CreateDepositRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            EndPoint.CREATE_DEPOSIT,
            ResponseSpecs.code_400()
        ).post(create_deposit_request)

    def create_transfer(self, create_user_request: CreateUserRequest, create_transfer_request: CreateTransferRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            EndPoint.CREATE_TRANSFER,
            ResponseSpecs.code_200()
        ).post(create_transfer_request)
        return response

    def create_transfer_invalid(self, create_user_request: CreateUserRequest,
                                create_transfer_request: CreateTransferRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            EndPoint.CREATE_TRANSFER,
            ResponseSpecs.code_404()
        ).post(create_transfer_request)

    def create_credit(self, create_user_secret_request: CreateUserRequest, create_credit_request: CreateCreditRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_secret_request.username,
                                      password=create_user_secret_request.password),
            EndPoint.CREATE_CREDIT,
            ResponseSpecs.code_201()
        ).post(create_credit_request)
        return response

    def create_credit_invalid(self, create_user_secret_request: CreateUserRequest,
                              create_credit_request: CreateCreditRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_secret_request.username,
                                      password=create_user_secret_request.password),
            EndPoint.CREATE_CREDIT,
            ResponseSpecs.code_400()
        ).post(create_credit_request)

    def create_credit_repay(self, create_user_secret_request: CreateUserRequest,
                            credit_repay_request: CreditRepayRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_secret_request.username,
                                      password=create_user_secret_request.password),
            EndPoint.CREATE_CREDIT_REPAY,
            ResponseSpecs.code_200()
        ).post(credit_repay_request)
        return response

    def create_credit_repay_invalid(self, create_user_secret_request: CreateUserRequest,
                            credit_repay_request: CreditRepayRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_secret_request.username,
                                      password=create_user_secret_request.password),
            EndPoint.CREATE_CREDIT_REPAY,
            ResponseSpecs.code_422()
        ).post(credit_repay_request)

    def get_transactions(self, create_user_request: CreateUserRequest, account_id: int):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            EndPoint.GET_TRANSACTIONS,
            ResponseSpecs.code_200()
        ).get(path_suffix=str(account_id))
        return response

    def get_credit_history(self, create_user_secret_request: CreateUserRequest) -> GetCreditHistoryResponse:
        return ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_secret_request.username, password=create_user_secret_request.password),
            EndPoint.GET_CREDIT_HISTORY,
            ResponseSpecs.code_200(),
        ).get()


