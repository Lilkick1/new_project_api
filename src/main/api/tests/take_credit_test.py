import pytest

from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_credit_account_request import CreateCreditUserRequest



@pytest.mark.api
class TestTakeCredit:

    def test_take_credit(self,  api_manager, create_credit_user_request):
        response = api_manager.user_steps.create_account(create_credit_user_request)

        assert response.balance == 0