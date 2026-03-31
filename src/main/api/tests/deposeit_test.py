import pytest

from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.deposit_request import DepositRequest


@pytest.mark.api
class TestDeposit:
    @pytest.mark.parametrize('amount', [1000.50, 9000])
    def test_deposit(self, api_manager, create_user_request: CreateUserRequest, create_account_user_id, amount):
        deposit_account_request = DepositRequest(accountId=create_account_user_id, amount=amount)
        response = api_manager.user_steps.deposit(create_user_request, deposit_account_request)
        # Проверка что баланс = зачислению
        assert response.balance == amount
        # Проверяем, что id операции вернулся
        assert response.id is not None

    @pytest.mark.parametrize('amount', [999.9, 9000.1])
    def test_invalid_deposit(self, api_manager, create_user_request: CreateUserRequest, create_account_user_id, amount):
        deposit_account_request = DepositRequest(accountId=create_account_user_id, amount=amount)
        api_manager.user_steps.invalid_deposit(create_user_request, deposit_account_request)