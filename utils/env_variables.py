import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Access environment variables
MAILTRAP_HOST = os.getenv("MAILTRAP_HOST")
MAILTRAP_PORT = os.getenv("MAILTRAP_PORT")
MAILTRAP_USERNAME = os.getenv("MAILTRAP_USERNAME")
MAILTRAP_PASSWORD = os.getenv("MAILTRAP_PASSWORD")