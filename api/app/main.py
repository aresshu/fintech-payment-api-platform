from fastapi import FastAPI
from app.routes import health_router, transactions_router

app = FastAPI()

app.include_router(health_router)
app.include_router(transactions_router)
