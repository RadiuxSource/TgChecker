import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List, Optional

load_dotenv()

class Settings(BaseModel):
    # Telegram API
    API_ID: int = Field(..., env="API_ID")
    API_HASH: str = Field(..., env="API_HASH")
    BOT_TOKEN: str = Field(..., env="BOT_TOKEN")
    
    # Database
    DB_URL: str = Field(
        default="sqlite+aiosqlite:///database.db",
        env="DB_URL"
    )
    
    # Channels
    UPDATE_CHANNEL: str = Field(
        default="ScienceStudyRoom",
        env="UPDATE_CHANNEL"
    )
    SUPPORT_CHAT: str = Field(
        default="BotSupport",
        env="SUPPORT_CHAT"
    )
    LOG_CHANNEL: Optional[str] = Field(
        default=None,
        env="LOG_CHANNEL"
    )
    
    # Payments
    STRIPE_SECRET: Optional[str] = Field(
        default=None,
        env="STRIPE_SECRET"
    )
    STRIPE_PRICE_ID: Optional[str] = Field(
        default=None,
        env="STRIPE_PRICE_ID"
    )
    
    # Admin
    ADMIN_IDS: List[int] = Field(
        default_factory=list,
        env="ADMIN_IDS"
    )

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        extra = 'ignore'

# Initialize config
try:
    Config = Settings()
except Exception as e:
    print(f"Error loading config: {e}")
    raise
