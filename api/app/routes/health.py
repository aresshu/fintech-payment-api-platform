from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter(
    prefix="/health",
    tags=["health"]
)

class HealthResponse(BaseModel):
    status: str
    message: str

@router.get("", response_model=HealthResponse, status_code=status.HTTP_200_OK)
def get_health():
    return HealthResponse(
        status="ok",
        message="Service is healthy and running"
    )