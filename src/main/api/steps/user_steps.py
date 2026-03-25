from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.models.deposit_transfer_request import DepositTransferRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.resnonse_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps



class UserSteps(BaseSteps):
    def create_account(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_create()
        ).post()
        return response

    def deposit(self, deposit_request: DepositRequest, username: str, password: str):
        response = ValidateCrudRequester(
            request_spec=RequestSpecs.auth_headers(username=username, password=password),
            endpoint=Endpoint.CREATE_DEPOSIT,
            response_spec=ResponseSpecs.request_ok()
        ).post(deposit_request)
        return response

    def invalid_deposit(self, deposit_request: DepositRequest, username: str, password: str):
        response = CrudRequester(
            request_spec=RequestSpecs.auth_headers(username=username, password=password),
            endpoint=Endpoint.CREATE_DEPOSIT,
            response_spec=ResponseSpecs.request_bad()
        ).post(deposit_request)
        return response

    def deposit_transfer(self, deposit_transfer_request: DepositTransferRequest, username: str, password: str):
        response = ValidateCrudRequester(
            request_spec=RequestSpecs.auth_headers(username=username, password=password),
            endpoint=Endpoint.DEPOSIT_TRANSFER,
            response_spec=ResponseSpecs.request_ok()
        ).post(deposit_transfer_request)
        return response

