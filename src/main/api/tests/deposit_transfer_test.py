import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.account_crud import AccountCrudDb as Account
from src.main.api.db.crud.transaction_crud import TransactionCrudDb as Transaction
from src.main.api.models.create_user_request import CreateUserRequest


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
    def test_transfer_between_accounts(self, api_manager: ApiManager, db_session: Session, create_user_request: CreateUserRequest, prepared_transfer, transfer_request):


        transfer_response = api_manager.user_steps.deposit_transfer(create_user_request, transfer_request)


        assert transfer_response.fromAccountId == prepared_transfer.account1.id
        assert transfer_response.toAccountId == prepared_transfer.account2.id
        expected_balance = prepared_transfer.actual_balance_after_deposit - transfer_request.amount
        assert transfer_response.fromAccountIdBalance == expected_balance

        transaction_from_db = Transaction.get_last_transaction_by_account(db_session, prepared_transfer.account1.id, transaction_type="transfer")
        assert transaction_from_db.amount == transfer_request.amount
        assert transaction_from_db.from_account_id == prepared_transfer.account1.id
        assert transaction_from_db.to_account_id == prepared_transfer.account2.id
        account_from_db = Account.get_account_by_id(db_session, prepared_transfer.account2.id)
        assert account_from_db.balance == transfer_request.amount

    @pytest.mark.parametrize(
        'transfer_request',
        [
            {'amount': 499},
            {'amount': 10001}
        ],
        indirect=True
    )
    def test_bad_transfer_between_accounts(self, api_manager: ApiManager, db_session: Session, create_user_request: CreateUserRequest, prepared_transfer, transfer_request):

        api_manager.user_steps.deposit_transfer_invalid(create_user_request, transfer_request)

        account_from_db = Account.get_account_by_id(db_session, prepared_transfer.account1.id)
        assert account_from_db.balance == prepared_transfer.actual_balance_after_deposit

