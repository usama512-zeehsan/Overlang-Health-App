from fastapi import APIRouter, HTTPException
from models.quiz import EmailCapture
import smtplib
from email.mime.text import MIMEText
import os
from utils.env_variables import MAILTRAP_HOST, MAILTRAP_PORT, MAILTRAP_USERNAME, MAILTRAP_PASSWORD

router = APIRouter()

SENDER_EMAIL = "OverLang AI <noreply@overlang.ai>"

@router.post("/capture-email")
def capture_email(payload: EmailCapture):
    if not payload.email:
        raise HTTPException(status_code=400, detail="Email is required.")

    subject = "Your AI-Powered Health Report"
    body = f"""
Hi there,

Thank you for completing the OverLang AI Health Quiz.

Your personalized recommendations will be processed shortly. This message confirms your email capture.

Stay well,  
OverLang AI Team
"""

    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = SENDER_EMAIL
    message["To"] = payload.email

    try:
        with smtplib.SMTP(MAILTRAP_HOST, MAILTRAP_PORT) as server:
            server.starttls()  # STARTTLS for secure connection
            server.login(MAILTRAP_USERNAME, MAILTRAP_PASSWORD)
            server.sendmail(SENDER_EMAIL, payload.email, message.as_string())

        return {"message": f"Email sent to {payload.email} successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Email failed to send: {str(e)}")
