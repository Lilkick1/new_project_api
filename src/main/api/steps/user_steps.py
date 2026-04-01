from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.create_credit_user_request import CreateCreditUserRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest
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

    def create_credit_account(self, create_credit_user_request: CreateCreditUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_credit_user_request.username, password=create_credit_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_create()
        ).post()
        return response

    def deposit(self,create_user_request: CreateUserRequest, deposit_request: DepositRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            endpoint=Endpoint.CREATE_DEPOSIT,
            response_spec=ResponseSpecs.request_ok()
        ).post(deposit_request)
        return response

    def invalid_deposit(self, create_user_request: CreateUserRequest, deposit_request: DepositRequest):
        response = CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            endpoint=Endpoint.CREATE_DEPOSIT,
            response_spec=ResponseSpecs.request_bad()
        ).post(deposit_request)
        return response

    def deposit_transfer(self, create_user_request: CreateUserRequest, deposit_transfer_request: DepositTransferRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            endpoint=Endpoint.DEPOSIT_TRANSFER,
            response_spec=ResponseSpecs.request_ok()
        ).post(deposit_transfer_request)
        return response

    def deposit_transfer_invalid(self, create_user_request: CreateUserRequest, deposit_transfer_request: DepositTransferRequest):
        response = CrudRequester(
            request_spec=RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            endpoint=Endpoint.DEPOSIT_TRANSFER,
            response_spec=ResponseSpecs.request_bad()
        ).post(deposit_transfer_request)
        return response

    def take_credit(self, create_credit_user_request: CreateCreditUserRequest, credit_request: CreditRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_credit_user_request.username, password=create_credit_user_request.password),
            endpoint=Endpoint.TAKE_CREDIT,
            response_spec=ResponseSpecs.request_create()
        ).post(credit_request)
        return response

    def take_credit_invalid(self, create_credit_user_request: CreateCreditUserRequest, credit_request: CreditRequest):
        response = CrudRequester(
            RequestSpecs.auth_headers(username=create_credit_user_request.username,
                                      password=create_credit_user_request.password),
            endpoint=Endpoint.TAKE_CREDIT,
            response_spec=ResponseSpecs.request_bad()
        ).post(credit_request)
        return response

    def credit_repay(self, create_credit_user_request: CreateCreditUserRequest, credit_repay_request: CreditRepayRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_credit_user_request.username, password=create_credit_user_request.password),
            endpoint=Endpoint.CREDIT_REPAY,
            response_spec=ResponseSpecs.request_ok()
        ).post(credit_repay_request)
        return response
    def credit_repay_invalid(self, create_credit_user_request: CreateCreditUserRequest, credit_repay_request: CreditRepayRequest):
        response = CrudRequester(
            RequestSpecs.auth_headers(username=create_credit_user_request.username, password=create_credit_user_request.password),
            endpoint=Endpoint.CREDIT_REPAY,
            response_spec=ResponseSpecs.request_bad()
        ).post(credit_repay_request)
        return response

