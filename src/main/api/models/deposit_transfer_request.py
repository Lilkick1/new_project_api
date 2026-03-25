from src.main.api.models.base_model import BaseModel


class DepositTransferRequest(BaseModel):
    fromAccountId: int
    toAccountId: int
    amount: float