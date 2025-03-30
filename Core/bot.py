from pyrogram import Client
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from pyrogram.filters import command, regex
from config import Config
from Database.session import AsyncSessionLocal
from Modules import (
    start, 
    force_sub,
    admin,
    channels,
    payments,
    analytics
)
from Core.decorators import handle_errors
from Core.utils import send_log

class TgCheckerBot:
    def __init__(self):
        self.client = Client(
            name="TgCheckerBot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            plugins=dict(root="Modules")
        )
        self._setup_handlers()

    def _setup_handlers(self):
        """Register all handlers with proper filters"""
        self.client.add_handler(MessageHandler(
            start.handle_start,
            command("start") & filters.private
        ))
        
        self.client.add_handler(CallbackQueryHandler(
            admin.handle_admin_callback,
            regex(r"^admin_")
        ))
        
        self.client.add_handler(MessageHandler(
            force_sub.check_member,
            filters.group
        ))
        
        self.client.add_handler(CallbackQueryHandler(
            channels.handle_channel_callback,
            regex(r"^channel_")
        ))
        
        self.client.add_handler(CallbackQueryHandler(
            payments.handle_payment_callback,
            regex(r"^payment_")
        ))

    @handle_errors
    async def start(self):
        """Start the bot client"""
        await self.client.start()
        await send_log("Bot started successfully")
        
        # Set bot commands
        await self.client.set_bot_commands([
            ("start", "Start the bot"),
            ("settings", "Configure bot settings"),
            ("stats", "View statistics")
        ])

    @handle_errors
    async def stop(self):
        """Stop the bot client"""
        if hasattr(self.client, 'is_initialized') and self.client.is_initialized:
            await send_log("Bot stopping...")
            await self.client.stop()
