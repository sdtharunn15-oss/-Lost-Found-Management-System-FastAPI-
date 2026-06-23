from fastapi import APIRouter, Depends

from app.dependencies import get_current_user

router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"]
)


@router.get("/profile")
def profile(
    current_user=Depends(get_current_user)
):
    return current_user