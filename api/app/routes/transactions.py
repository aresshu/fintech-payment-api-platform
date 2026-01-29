from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
import uuid

# Pydantic models
class TransactionRequest(BaseModel):
    amount: float
    currency: str

class TransactionResponse(BaseModel):
    transaction_id: str

# In-memory storage for transactions
transactions: List[dict] = []

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)

@router.post("", response_model=TransactionResponse)
def create_transaction(transaction: TransactionRequest): 
    transaction_id = str(uuid.uuid4())

    transaction_data = {
        "transaction_id": transaction_id,
        "amount": transaction.amount,
        "currency": transaction.currency
    }

    transactions.append(transaction_data)

    return TransactionResponse(transaction_id=transaction_id)
