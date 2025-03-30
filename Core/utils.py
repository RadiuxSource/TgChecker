import asyncio
from datetime import datetime
from pyrogram import Client
from pyrogram.types import Message
from config import Config
from Templates.messages import LOG_TEMPLATE

async def send_log(text: str, level: str = "INFO"):
    """Send log message to admin/log channel"""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = LOG_TEMPLATE.format(
            timestamp=timestamp,
            level=level,
            message=text
        )
        async with Client("logger", Config.API_ID, Config.API_HASH) as client:
            await client.send_message(Config.LOG_CHANNEL, log_message)
    except Exception as e:
        print(f"Failed to send log: {e}")

async def delete_message_after(message: Message, seconds: int):
    """Delete message after specified time"""
    await asyncio.sleep(seconds)
    try:
        await message.delete()
    except:
        pass

def format_time(seconds: int) -> str:
    """Convert seconds to human-readable time"""
    periods = [
        ('year', 60*60*24*365),
        ('month', 60*60*24*30),
        ('day', 60*60*24),
        ('hour', 60*60),
        ('minute', 60),
        ('second', 1)
    ]
    parts = []
    for period_name, period_seconds in periods:
        if seconds >= period_seconds:
            period_value, seconds = divmod(seconds, period_seconds)
            plural = 's' if period_value > 1 else ''
            parts.append(f"{period_value} {period_name}{plural}")
    return ", ".join(parts) if parts else "0 seconds"
