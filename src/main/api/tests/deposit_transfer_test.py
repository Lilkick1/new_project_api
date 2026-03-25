import pytest
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.models.deposit_transfer_request import DepositTransferRequest


@pytest.mark.api
class TestDepositTransfer:
    def test_deposit_transfer(self, api_manager, create_user_request):
        # 1. Создаем два счета
        account1 = api_manager.user_steps.create_account(create_user_request)
        account2 = api_manager.user_steps.create_account(create_user_request)

        # 2. Вносим депозит на первый счет
        deposit_request = DepositRequest(
            accountId=account1.id,
            amount=1000.50
        )

        api_manager.user_steps.deposit(
            deposit_request=deposit_request,
            username=create_user_request.username,
            password=create_user_request.password
        )

        # 3. Создаем запрос на перевод
        transfer_request = DepositTransferRequest(
            fromAccountId=account1.id,
            toAccountId=account2.id,
            amount=500.00
        )

        # 4. Выполняем перевод
        response = api_manager.user_steps.deposit_transfer(
            deposit_transfer_request=transfer_request,
            username=create_user_request.username,
            password=create_user_request.password
        )

        # 5. Проверки
        assert response.fromAccountId == account1.id
        assert response.toAccountId == account2.id
        assert response.fromAccountIdBalance == 500.50  # 1000.50 - 500.00