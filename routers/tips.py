from fastapi import APIRouter
from services.streaks import get_daily_tip

router = APIRouter()

@router.get("/daily-tip")
def daily_tip():
    return {"tip": get_daily_tip()}
