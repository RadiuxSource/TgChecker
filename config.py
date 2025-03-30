import os
from dotenv import load_dotenv

# Load environment variables from .env file if available
load_dotenv()

# Bot API details
API_ID = int(os.getenv("API_ID", 123456))  # Replace with your actual API ID
API_HASH = os.getenv("API_HASH", "your_api_hash")  # Replace with your actual API hash
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")  # Replace with your actual bot token

# Database (MongoDB) configuration
MONGO_URI = os.getenv("MONGO_URI", "your_mongodb_uri")
DATABASE_NAME = os.getenv("DATABASE_NAME", "TgCheckerDB")

# Owner and Logging
OWNER_ID = int(os.getenv("OWNER_ID", 123456789))  # Replace with your actual owner ID
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", -1001234567890))  # Replace with actual log group ID
OWNER_CHANNEL = os.getenv("OWNER_CHANNEL", "@ScienceStudyRoom")  # Your channel name

# Force Subscription Configuration
QUIZZORA_BOT = os.getenv("QUIZZORA_BOT", "@QuizzoraBot")  # Bot that must be added
MAX_FREE_CHANNELS = int(os.getenv("MAX_FREE_CHANNELS", 2))  # Free limit
SUBSCRIPTION_PRICE = os.getenv("SUBSCRIPTION_PRICE", "5 USD/month")  # Change as required
TOKEN_VERIFICATION_REQUIRED = os.getenv("TOKEN_VERIFICATION_REQUIRED", "True").lower() == "true"

# Other Settings
BOT_SUPPORT_GROUP = os.getenv("BOT_SUPPORT_GROUP", "@BotSupport")
BOT_UPDATES_CHANNEL = os.getenv("BOT_UPDATES_CHANNEL", "@BotUpdates")

# Science Study Room