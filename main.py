from pyrogram import Client, filters
import config
from Core.logger import logger
from Modules import member_checker  # Import the member checker module

# Initialize bot
bot = Client(
    "MemberCheckerBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

@bot.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Hello! I am a Member Checker Bot. Use /check to verify your membership.")

if __name__ == "__main__":
    logger.info("Bot is starting...")
    bot.run()
    logger.info("Bot has started successfully.")
    logger.info("Bot is running...")
    logger.info("Bot is ready to accept commands.")