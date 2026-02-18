from typing import List, Optional

from src.main.api.models.base_model import BaseModel


class TransactionItem(BaseModel):
    transactionId: int
    type: str
    amount: float
    fromAccountId: Optional[int] = None
    toAccountId: Optional[int] = None
    createdAt: str
    creditId: Optional[int] = None


class GetTransactionsResponse(BaseModel):
    id: int
    number: str
    balance: float
    transactions: List[TransactionItem]
