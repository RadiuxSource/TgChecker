#!/usr/bin/env python3
import asyncio
import logging
from pathlib import Path
from pyrogram import idle
from Core.bot import TgCheckerBot
from Database.session import init_db
from config import Config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

async def main():
    """Main entry point for the bot"""
    try:
        # Verify config
        if not all([Config.API_ID, Config.API_HASH, Config.BOT_TOKEN]):
            raise ValueError("Missing required configuration values")
        
        # Initialize database
        await init_db()
        logger.info("✅ Database initialized")
        
        # Create bot instance
        bot = TgCheckerBot()
        logger.info("✅ Bot instance created")
        
        # Start the bot
        await bot.start()
        logger.info("✅ Bot started successfully")
        
        # Run until stopped
        await idle()
        
    except KeyboardInterrupt:
        logger.info("🛑 Received stop signal, shutting down...")
    except Exception as e:
        logger.error(f"❌ Fatal error: {str(e)}", exc_info=True)
    finally:
        if 'bot' in locals():
            await bot.stop()
            logger.info("🛑 Bot stopped successfully")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.error(f"❌ Critical error: {str(e)}", exc_info=True)
