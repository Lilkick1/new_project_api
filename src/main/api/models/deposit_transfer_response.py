from src.main.api.models.base_model import BaseModel


class DepositTransferResponse(BaseModel):
    fromAccountId: int
    toAccountId: int
    fromAccountIdBalance: float