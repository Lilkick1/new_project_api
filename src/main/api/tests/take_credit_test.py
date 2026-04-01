import pytest
from requests import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_credit_user_request import CreateCreditUserRequest
from src.main.api.models.credit_request import CreditRequest
from src.main.api.db.crud.credit_crud import CreditCrudDb as Credit
from src.main.api.db.crud.account_crud import AccountCrudDb as Account


@pytest.mark.api
class TestTakeCredit:
    @pytest.mark.parametrize('amount, termMonths', [
        (5000.00, 12),
        (10000.00, 24),
        (15000.00, 36),
    ])
    def test_take_credit(self,db_session: Session, api_manager: ApiManager, create_credit_user_request: CreateCreditUserRequest, create_credit_account_user_id, amount, termMonths):
        credit_request = CreditRequest(accountId=create_credit_account_user_id, amount=amount, termMonths=termMonths)
        response = api_manager.user_steps.take_credit(create_credit_user_request, credit_request)

        assert response.balance == amount

        credit_from_db = Credit.get_credit_by_id(db_session, response.creditId)
        assert credit_from_db.balance == -amount
        assert credit_from_db.amount == amount

    @pytest.mark.parametrize('amount, termMonths', [
        (4999.00, 12),
        (15001.00, 36),
    ])
    def test_take_credit_invalid(self, db_session: Session, api_manager: ApiManager,
                         create_credit_user_request: CreateCreditUserRequest, create_credit_account_user_id, amount,
                         termMonths):
        credit_request = CreditRequest(accountId=create_credit_account_user_id, amount=amount, termMonths=termMonths)
        response = api_manager.user_steps.take_credit_invalid(create_credit_user_request, credit_request)

        account_from_db = Account.get_account_by_id(db_session, create_credit_account_user_id)
        assert account_from_db.balance == 0