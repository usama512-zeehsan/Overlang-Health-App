from sqlalchemy import Column, Integer, String, DateTime, JSON
from database import Base
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableList  # ✅ import this
from datetime import datetime
from pydantic import BaseModel

class UserSession(Base):
    __tablename__ = "user_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, unique=True, index=True)
    user_id = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    questions = Column(MutableList.as_mutable(JSONB), default=list, nullable=False)  # ✅
    responses = Column(MutableList.as_mutable(JSONB), default=list, nullable=False)  # ✅

class SessionAppendRequest(BaseModel):
    session_id: str
    question: str
    answer: str