from fastapi import FastAPI
from app.routes import health_router, transactions_router
from app.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
)

app.include_router(health_router)
app.include_router(transactions_router)
