from fastapi import FastAPI
from routers import quiz, tips, email, session as session_router, recommendations
from models import session as session_model, recommendation as recommendation_model
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="OverLang AI Quiz Backend")

app.include_router(quiz.router, prefix="/api")
app.include_router(tips.router, prefix="/api")
app.include_router(email.router, prefix="/api")
app.include_router(session_router.router, prefix="/api")  # register session routes
app.include_router(recommendations.router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "OK"}
