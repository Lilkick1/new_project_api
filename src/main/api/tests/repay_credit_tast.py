import pytest

from src.main.api.models.create_credit_user_request import CreateCreditUserRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest



@pytest.mark.api
class TestCreditRepay:
    @pytest.mark.parametrize('amount', [1000, 5000])
    def test_credit_repay(self, api_manager, create_credit_user_request: CreateCreditUserRequest, credit_for_repay, amount):
        repay_request = CreditRepayRequest(creditId=credit_for_repay.credit_id, accountId=credit_for_repay.account_id, amount=amount)
        response = api_manager.user_steps.credit_repay(create_credit_user_request, repay_request)

        assert response.creditId == credit_for_repay.credit_id
        assert response.amountDeposited == amount
        assert response.amountDeposited <= credit_for_repay.credit_amount

