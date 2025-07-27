from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from sqlalchemy import text  # ✅ ADD THIS IMPORT
from models.session import UserSession, SessionAppendRequest
import uuid

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/session/start")
def start_session(user_id: str, db: Session = Depends(get_db)):
    session_id = str(uuid.uuid4())
    new_session = UserSession(session_id=session_id, user_id=user_id, questions=[], responses=[])
    db.add(new_session)
    db.commit()
    return {"session_id": session_id}

@router.post("/session/append")
def append_to_session(payload: SessionAppendRequest, db: Session = Depends(get_db)):
    session = db.query(UserSession).filter(UserSession.session_id == payload.session_id).first()
    if session:
        session.questions.append(payload.question)
        session.responses.append({
            "question": payload.question,
            "answer": payload.answer
        })
        db.commit()
        return {"message": "Updated"}
    return {"error": "Session not found"}

@router.get("/health/db")
def check_db_connection(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))  # ✅ wrap in text()
        return {"status": "Database connected"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))