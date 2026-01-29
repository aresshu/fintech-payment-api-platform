from pydantic import BaseModel

class TransactionCreate(BaseModel):
    amount: float
    currency: str

class TransactionResponse(BaseModel):
    transaction_id: str
    amount: float
    currency: str