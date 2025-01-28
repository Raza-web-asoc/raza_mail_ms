import os
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

class Settings:
    SMTP_SERVER: str = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", 587))  # Puerto estándar TLS
    SMTP_USERNAME: str = os.getenv("SMTP_USERNAME")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD")
    EMAIL_FROM: str = os.getenv("EMAIL_FROM", SMTP_USERNAME)

settings = Settings()