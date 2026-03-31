import pytest

from src.main.api.models.deposit_response import DepositResponse


@pytest.mark.api
class TestTransfer:

    @pytest.mark.parametrize(
        'transfer_request',
        [
            {'amount': 500},
            {'amount': 1000},
            {'amount': 2500.50}
        ],
        indirect=True
    )
    def test_transfer_between_accounts(self, api_manager, create_user_request, prepared_transfer, transfer_request):


        transfer_response = api_manager.user_steps.deposit_transfer(create_user_request, transfer_request)


        assert transfer_response.fromAccountId == prepared_transfer.account1.id
        assert transfer_response.toAccountId == prepared_transfer.account2.id
        expected_balance = prepared_transfer.actual_balance_after_deposit - transfer_request.amount
        assert transfer_response.fromAccountIdBalance == expected_balance

    @pytest.mark.parametrize(
        'transfer_request',
        [
            {'amount': 499},
            {'amount': 10001}
        ],
        indirect=True
    )
    def test_bad_transfer_between_accounts(self, api_manager, create_user_request, prepared_transfer, transfer_request):

        api_manager.user_steps.deposit_transfer_invalid(create_user_request, transfer_request)

