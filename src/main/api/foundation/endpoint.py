from dataclasses import dataclass
from enum import Enum
from typing import Optional, Type
from src.main.api.models.base_model import BaseModel
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_response import CreateUserResponse
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.models.deposit_response import DepositResponse
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.models.login_user_response import LoginUserResponse


@dataclass
class EndPointConfiguration:
    url: str
    request_model: Optional[Type[BaseModel]]
    response_model: Optional[Type[BaseModel]]


class Endpoint(Enum):
    ADMIN_CRATE_USER = EndPointConfiguration(
        request_model=CreateUserRequest,
        url="/admin/create",
        response_model=CreateUserResponse
    )

    ADMIN_DELETE_USER = EndPointConfiguration(
        request_model=None,
        url="/admin/users",
        response_model=None
    )

    LOGIN_USER = EndPointConfiguration(
        request_model=LoginUserRequest,
        url="/auth/token/login",
        response_model=LoginUserResponse
    )

    CREATE_ACCOUNT = EndPointConfiguration(
        request_model=None,
        url="/account/create",
        response_model=CreateAccountResponse
    )

    CREATE_DEPOSIT = EndPointConfiguration(
        request_model=DepositRequest,
        url='/account/deposit',
        response_model=DepositResponse
    )