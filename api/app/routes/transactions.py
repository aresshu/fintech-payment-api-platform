from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlmodel import Session, select
from app.models import Transaction
from app.db import get_session

import uuid

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
def create_transaction(transaction: PostTransactionRequest, session: Session = Depends(get_session)):
    transaction_id = str(uuid.uuid4())

    db_transaction = Transaction(
        transaction_id=transaction_id,
        amount=transaction.amount,
        currency=transaction.currency
    )

    session.add(db_transaction)
    session.commit()
    session.refresh(db_transaction)

    return PostTransactionResponse(transaction_id=transaction_id)

@router.get("/{trans_id}", response_model=GetTransactionResponse)
def get_transaction(trans_id: str, session: Session = Depends(get_session)):
    db_transaction = session.exec(select(Transaction).where(Transaction.transaction_id == trans_id)).first()

    if not db_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return GetTransactionResponse(
        transaction_id=db_transaction.transaction_id,
        amount=db_transaction.amount,
        currency=db_transaction.currency
    )