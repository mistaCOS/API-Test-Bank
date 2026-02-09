from src.main.api.models.base_model import BaseModel



class CreateTransferResponse(BaseModel):
    fromAccountId: int
    toAccountId: int
    fromAccountIdBalance: float