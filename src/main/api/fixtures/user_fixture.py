import pytest

from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.models.deposit_transfer_request import DepositTransferRequest


@pytest.fixture
def create_user_request(api_manager):
    user_request = (RandomModelGenerator.generate(CreateUserRequest))
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def deposit_request(create_user_request, api_manager, request):
    """Создает счет и возвращает запрос на депозит"""
    params = getattr(request, 'param', {})
    amount = params.get('amount', 1000.50)
    account = api_manager.user_steps.create_account(create_user_request)
    return DepositRequest(
        accountId=account.id,
        amount=amount
    )

@pytest.fixture
def transfer_request(create_two_accounts, request):
    """Создает запрос на перевод"""
    params = getattr(request, 'param', {})
    amount = params.get('amount', 1000.50)
    account1, account2 = create_two_accounts
    return DepositTransferRequest(
        fromAccountId=account1.id,
        toAccountId=account2.id,
        amount=amount
    )

