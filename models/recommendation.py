# models/recommendation.py

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class RecommendationRecord(Base):
    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, ForeignKey("user_sessions.session_id"), nullable=False)
    user_id = Column(String, nullable=False)
    recommendation = Column(JSONB, nullable=False)
    responses = Column(JSONB, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class RecommendationCreate(BaseModel):
    user_id: str
    goal: str
    tips: List[str]
    products: List[str]
    call_to_action: Optional[str] = None

class RecommendationResponse(RecommendationCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True