import pytest
from sqlalchemy.orm import Session
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.db.crud.account_crud import AccountCrudDb as Account


@pytest.mark.api
class TestDeposit:
    @pytest.mark.parametrize('amount', [1000.50, 9000])
    def test_deposit(self, api_manager: ApiManager, db_session: Session, create_user_request: CreateUserRequest, create_account_user_id, amount):
        deposit_account_request = DepositRequest(accountId=create_account_user_id, amount=amount)
        response = api_manager.user_steps.deposit(create_user_request, deposit_account_request)
        # Проверка что баланс = зачислению
        assert response.balance == amount
        # Проверяем, что id операции вернулся
        assert response.id is not None

        account_from_db = Account.get_account_by_id(db_session, create_account_user_id)
        assert account_from_db.id == create_account_user_id
        assert account_from_db.balance == amount



    @pytest.mark.parametrize('amount', [999.9, 9000.1])
    def test_invalid_deposit(self, api_manager: ApiManager, db_session: Session, create_user_request: CreateUserRequest, create_account_user_id, amount):
        deposit_account_request = DepositRequest(accountId=create_account_user_id, amount=amount)
        api_manager.user_steps.invalid_deposit(create_user_request, deposit_account_request)

        account_from_db = Account.get_account_by_id(db_session, create_account_user_id)
        assert account_from_db.id == create_account_user_id
        assert account_from_db.balance == 0