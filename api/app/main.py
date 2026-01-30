from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes import health_router, transactions_router
from app.config import settings
from app.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    print("goodbye from lifespan")

app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan
)

app.include_router(health_router)
app.include_router(transactions_router)
