import os
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    # Telegram API
    API_ID: int = int(os.getenv("API_ID"))
    API_HASH: str = os.getenv("API_HASH")
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")
    
    # Database
    DB_URL: str = os.getenv("DB_URL", "sqlite+aiosqlite:///database.db")
    
    # Channels
    UPDATE_CHANNEL: str = os.getenv("UPDATE_CHANNEL", "ScienceStudyRoom")
    SUPPORT_CHAT: str = os.getenv("SUPPORT_CHAT", "BotSupport")
    
    # Payments
    PAYMENT_PROVIDER: str = os.getenv("PAYMENT_PROVIDER", "stripe")
    STRIPE_SECRET: str = os.getenv("STRIPE_SECRET")
    
    # Security
    ADMIN_IDS: list = list(map(int, os.getenv("ADMIN_IDS", "").split(',')))
    
    class Config:
        env_file = ".env"

Config = Settings()
