from fastapi import APIRouter, HTTPException
from typing import List
from models.quiz import QuizResponse
from models.response import Recommendation
from services.recommendations import generate_recommendations

router = APIRouter()

@router.post("/recommendations", response_model=Recommendation)
async def get_recommendations(responses: List[QuizResponse]):
    try:
        return generate_recommendations(responses)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
