import pytest
from requests import Session
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_credit_user_request import CreateCreditUserRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.db.crud.transaction_crud import TransactionCRUD as Transaction
from src.main.api.db.crud.account_crud import AccountCRUD as Account



@pytest.mark.api
class TestCreditRepay:
    @pytest.mark.parametrize('amount', [5000])
    def test_credit_repay(self, api_manager: ApiManager, db_session: Session, create_credit_user_request: CreateCreditUserRequest, credit_for_repay, amount):
        repay_request = CreditRepayRequest(creditId=credit_for_repay.credit_id, accountId=credit_for_repay.account_id, amount=amount)
        response = api_manager.user_steps.credit_repay(create_credit_user_request, repay_request)

        assert response.creditId == credit_for_repay.credit_id
        assert response.amountDeposited == amount
        assert response.amountDeposited <= credit_for_repay.credit_amount

        repay_from_db = Transaction.get_transaction_by_id(bd_session, credit_for_repay.credit_id)
        assert repay_from_db.amount == amount
        account_from_db = Account.get_account_by_id(db_session, credit_for_repay.account_id)
        assert account_from_db.balance == response.amountDeposited - amount

