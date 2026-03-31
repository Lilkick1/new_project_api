from requests import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.account_crud import AccountCrudDb as Account
import pytest

from src.main.api.models.create_credit_user_request import CreateCreditUserRequest
from src.main.api.models.create_user_request import CreateUserRequest


@pytest.mark.api
class TestCreateAccount:
    def test_create_account(self, db_session: Session, api_manager: ApiManager, create_user_request: CreateUserRequest):
        response = api_manager.user_steps.create_account(create_user_request)

        assert response.balance == 0

        account_from_db = Account.get_account_by_id(db_session, response.id)
        assert account_from_db.id == response.id, 'Аккаунт не создан, id нет в БД'
        assert account_from_db.balance is not None, 'Поле баланса для созданного аккаунта отсутсвует в БД'

    def test_create_credit_account(self, db_session: Session, api_manager: ApiManager, create_credit_user_request: CreateCreditUserRequest):
        response = api_manager.user_steps.create_credit_account(create_credit_user_request)

        assert response.balance == 0

        account_from_db = Account.get_account_by_id(db_session, response.id)
        assert account_from_db.id == response.id, 'Аккаунт не создан, id нет в БД'
        assert account_from_db.balance is not None, 'Поле баланса для созданного аккаунта отсутсвует в БД'

