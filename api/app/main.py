from fastapi import FastAPI
from app.routes import health_router, transactions_router
from app.config import settings
from app.db import init_db

app = FastAPI(
    title=settings.PROJECT_NAME,
)

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(health_router)
app.include_router(transactions_router)
