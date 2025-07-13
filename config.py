import os
from dotenv import load_dotenv

# Load environment variables from .env file (if present)
load_dotenv()

class Settings:
    PROJECT_NAME: str = "OverLang-HealthChatAssistant"
    API_V1_STR: str = "/api"
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    AI_MODEL: str = os.getenv("AI_MODEL", "gpt-4")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

settings = Settings()
