from src.main.api.models.base_model import BaseModel


class PreparedRepayCreditData(BaseModel):
    credit_id: int
    account_id: int
    credit_amount: float