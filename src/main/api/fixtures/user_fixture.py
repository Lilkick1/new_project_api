import pytest

from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_credit_user_request import CreateCreditUserRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.models.deposit_transfer_request import DepositTransferRequest
from src.main.api.models.prepared_repay_credit_data import PreparedRepayCreditData
from src.main.api.models.prepared_transfer_data import PreparedTransferData


@pytest.fixture
def create_user_request(api_manager):
    user_request = (RandomModelGenerator.generate(CreateUserRequest))
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def create_credit_user_request(api_manager):
    user_request = (RandomModelGenerator.generate(CreateCreditUserRequest))
    api_manager.admin_steps.create_credit_user(user_request)
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

@pytest.fixture
def create_account_user_id(api_manager, create_user_request):
    account = api_manager.user_steps.create_account(create_user_request)
    return account.id

@pytest.fixture
def create_credit_account_user_id(api_manager, create_credit_user_request):
    """Создаем счет для взятия кредита"""
    account = api_manager.user_steps.create_credit_account(create_credit_user_request)
    return account.id

@pytest.fixture
def create_two_accounts(api_manager, create_user_request):
    """Создает два счета для пользователя"""
    account1 = api_manager.user_steps.create_account(create_user_request)
    account2 = api_manager.user_steps.create_account(create_user_request)
    return account1, account2


@pytest.fixture
def prepared_transfer(api_manager, create_user_request, create_two_accounts, transfer_request):
    """Фикстура для перевода с фиксированным депозитом"""
    account1, account2 = create_two_accounts

    # Обновляем ID счетов в transfer_request
    transfer_request.fromAccountId = account1.id
    transfer_request.toAccountId = account2.id

    # Депозит: фиксированная сумма (например, 10000.00)
    DEPOSIT_AMOUNT = 9000

    # Вносим депозит
    deposit_request = DepositRequest(
        accountId=account1.id,
        amount=DEPOSIT_AMOUNT  # ← фиксированная сумма
    )

    deposit_response = api_manager.user_steps.deposit(
        create_user_request,
        deposit_request
    )

    # Возвращаем данные через Pydantic модель
    return PreparedTransferData(
        transfer_request=transfer_request,

        account1=account1,
        account2=account2,
        deposit_response=deposit_response,
        deposit_amount=DEPOSIT_AMOUNT,
        actual_balance_after_deposit=deposit_response.balance
    )

@pytest.fixture
def credit_for_repay(api_manager, create_credit_user_request, create_credit_account_user_id):
    credit_request = CreditRequest(
        accountId=create_credit_account_user_id,
        amount=5000,
        termMonths=12
    )

    credit_response = api_manager.user_steps.take_credit(
        create_credit_user_request,
        credit_request
    )


    deposit_amount = 5000  # достаточно для погашения 10000 кредита
    deposit_request = DepositRequest(
        accountId=create_credit_account_user_id,
        amount=deposit_amount
    )

    deposit_response = api_manager.user_steps.deposit(
        create_credit_user_request,
        deposit_request
    )
    print(f"Deposit response balance: {deposit_response.balance}")

    print(f"Credit response: {credit_response}")
    print(f"Credit ID: {credit_response.creditId}")
    print(f"=== DEBUG END ===\n")

    return PreparedRepayCreditData(
        credit_id=credit_response.creditId,
        account_id=create_credit_account_user_id,
        credit_amount=credit_request.amount
    )


