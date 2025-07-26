# routers/recommendation.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.recommendation import RecommendationRecord, RecommendationResponse
from models.session import UserSession
from database import SessionLocal
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class RecommendationOut(BaseModel):
    id: int
    session_id: str
    user_id: str
    goal: str
    tips: List[str]
    products: List[str]
    call_to_action: Optional[str]
    responses: List[dict]  # ✅ Changed from dict to List[dict]
    created_at: datetime   # Let Pydantic handle datetime serialization

    model_config = {
        "from_attributes": True  # ✅ Pydantic v2 equivalent of orm_mode
    }

class SaveRecommendationRequest(BaseModel):
    session_id: str
    user_id: str
    recommendation: dict
    responses: list

@router.post("/recommendation/save")
def save_recommendation(payload: SaveRecommendationRequest, db: Session = Depends(get_db)):
    new_record = RecommendationRecord(
        session_id=payload.session_id,
        user_id=payload.user_id,
        recommendation=payload.recommendation,
        responses=payload.responses,
        created_at=datetime.utcnow()
    )
    db.add(new_record)
    db.commit()
    return {"message": "Recommendation saved"}


@router.get("/recommendation/fetch", response_model=List[RecommendationOut])
def fetch_recommendations(user_id: str, db: Session = Depends(get_db)):
    records = db.query(RecommendationRecord).filter(RecommendationRecord.user_id == user_id).all()
    
    result = []
    for rec in records:
        rec_data = rec.recommendation
        result.append(RecommendationOut(
            id=rec.id,
            session_id=rec.session_id,
            user_id=rec.user_id,
            goal=rec_data.get("goal", ""),
            tips=rec_data.get("tips", []),
            products=rec_data.get("products", []),
            call_to_action=rec_data.get("call_to_action", ""),
            responses=rec.responses,  # assuming it's a list of dicts
            created_at=rec.created_at
        ))

    return result

@router.post("/recommendation/generate")
def generate_recommendation(session_id: str, user_id: str, db: Session = Depends(get_db)):
    session = db.query(UserSession).filter(UserSession.session_id == session_id).first()

    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    if not session.responses:
        raise HTTPException(status_code=400, detail="No responses found for this session")

    # 🧠 Stub: Simulate a recommendation from existing responses
    recommendation_payload = {
        "goal": "Improve your daily health routine",
        "tips": [
            "Drink at least 2L of water daily",
            "Get 8 hours of sleep",
            "Walk for 30 minutes every day"
        ],
        "products": [
            "Reusable Water Bottle",
            "Fitness Tracker"
        ],
        "call_to_action": "Start your wellness journey today!"
    }

    new_reco = RecommendationRecord(
        session_id=session_id,
        user_id=user_id,
        recommendation=recommendation_payload,
        responses=session.responses,
        created_at=datetime.utcnow()
    )

    db.add(new_reco)
    db.commit()

    return {"message": "Recommendation generated and saved"}