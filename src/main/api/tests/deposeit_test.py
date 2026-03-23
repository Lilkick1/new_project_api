import pytest


class TestDeposit:
    @pytest.mark.parametrize(
        'deposit_request',
        [
            {'amount': 1000.50},
            {'amount': 9000}
        ],
        indirect=True
    )
    def test_deposit(self, api_manager, create_user_request, deposit_request):
        response = api_manager.user_steps.deposit(
            deposit_request=deposit_request,
            username=create_user_request.username,
            password=create_user_request.password
        )
        # Проверка что баланс = зачислению
        assert response.balance == deposit_request.amount

        # Проверяем, что id операции вернулся
        assert response.id is not None

    @pytest.mark.parametrize(
        'deposit_request',
        [
            {'amount': 999.9},
            {'amount': 9000.1}
        ],
        indirect=True
    )
    def test_invalid_deposit(self, api_manager, create_user_request, deposit_request):
        response = api_manager.user_steps.invalid_deposit(
            deposit_request=deposit_request,
            username=create_user_request.username,
            password=create_user_request.password
        )