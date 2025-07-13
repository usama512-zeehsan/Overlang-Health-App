from fastapi import FastAPI
from routers import quiz, tips, email

app = FastAPI(title="OverLang AI Quiz Backend")

app.include_router(quiz.router, prefix="/api")
app.include_router(tips.router, prefix="/api")
app.include_router(email.router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "OK"}
