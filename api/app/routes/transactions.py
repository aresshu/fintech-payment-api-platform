from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

# In-memory storage for transactions
transactions: List[dict] = []

# Pydantic models
class PostTransactionRequest(BaseModel):
    amount: float
    currency: str

class PostTransactionResponse(BaseModel):
    transaction_id: str

class GetTransactionResponse(BaseModel):
    transaction_id: str
    amount: float
    currency: str

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)

@router.post("", response_model=PostTransactionResponse)
def create_transaction(transaction: PostTransactionRequest): 
    transaction_id = str(uuid.uuid4())

    transaction_data = {
        "transaction_id": transaction_id,
        "amount": transaction.amount,
        "currency": transaction.currency
    }

    transactions.append(transaction_data)

    return PostTransactionResponse(transaction_id=transaction_id)

@router.get("/{trans_id}", response_model=GetTransactionResponse)
def get_transaction(trans_id: str):
    for trans in transactions:
        if trans["transaction_id"] == trans_id:
            return GetTransactionResponse(**trans)

    raise HTTPException(status_code=404, detail="Transaction not found")