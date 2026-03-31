from typing import Any

from src.main.api.models.base_model import BaseModel



class PreparedTransferData(BaseModel):
    transfer_request: Any
    account1: Any
    account2: Any
    deposit_response: Any
    deposit_amount: int | float
    actual_balance_after_deposit: int | float
