from enum import Enum
from src.main.api.models.base_model import BaseModel
from typing import Optional
from dataclasses import dataclass

from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_credit_request import CreateCreditRequest
from src.main.api.models.create_credit_response import CreateCreditResponse
from src.main.api.models.create_deposit_request import CreateDepositRequest
from src.main.api.models.create_deposit_response import CreateDepositResponse
from src.main.api.models.create_transfer_request import CreateTransferRequest
from src.main.api.models.create_transfer_response import CreateTransferResponse
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_response import CreateUserResponse
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_repay_response import CreditRepayResponse
from src.main.api.models.delete_user_response import DeleteUserResponse
from src.main.api.models.get_credit_history_response import GetCreditHistoryResponse
from src.main.api.models.get_transactions_response import GetTransactionsResponse
from src.main.api.models.get_user_response import GetUserResponse
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.models.login_user_response import LoginUserResponse


@dataclass
class EndPointConfiguration:
    url: str
    request_model: Optional[BaseModel]
    response_model: Optional[BaseModel]


class EndPoint(Enum):
    ADMIN_CREATE_USER = EndPointConfiguration(
        url='/admin/create',
        request_model=CreateUserRequest,
        response_model=CreateUserResponse
    )

    ADMIN_DELETE_USER = EndPointConfiguration(
        request_model=None,
        url='/admin/users',
        response_model=DeleteUserResponse
    )

    LOGIN_USER = EndPointConfiguration(
        request_model=LoginUserRequest,
        url='/auth/token/login',
        response_model=LoginUserResponse
    )

    CREATE_ACCOUNT = EndPointConfiguration(
        request_model=None,
        url='/account/create',
        response_model=CreateAccountResponse
    )

    CREATE_DEPOSIT = EndPointConfiguration(
        request_model=CreateDepositRequest,
        url='/account/deposit',
        response_model=CreateDepositResponse
    )

    CREATE_TRANSFER = EndPointConfiguration(
        request_model=CreateTransferRequest,
        url='/account/transfer',
        response_model=CreateTransferResponse
    )

    CREATE_CREDIT = EndPointConfiguration(
        request_model=CreateCreditRequest,
        url='/credit/request',
        response_model=CreateCreditResponse
    )

    CREATE_CREDIT_REPAY = EndPointConfiguration(
        request_model=CreditRepayRequest,
        url='/credit/repay',
        response_model=CreditRepayResponse
    )

    GET_USER = EndPointConfiguration(
        request_model=None,
        url='/admin/users',
        response_model=GetUserResponse
    )

    GET_TRANSACTIONS = EndPointConfiguration(
        request_model=None,
        url='/account/transactions',
        response_model=GetTransactionsResponse
    )

    GET_CREDIT_HISTORY = EndPointConfiguration(
        request_model=None,
        url='/credit/history',
        response_model=GetCreditHistoryResponse
    )