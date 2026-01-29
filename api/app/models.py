from sqlmodel import SQLModel, Field

class Transaction(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    transaction_id: str 
    amount: float
    currency: str