from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import os

# Fetching environment variables from config.py
OWNER_ID = int(os.getenv("OWNER_ID", 123456789))  # Replace with actual owner ID
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "@ScienceStudySupport")
UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "@ScienceStudyUpdates")
PROMOTION_CHANNEL = os.getenv("PROMOTION_CHANNEL", "@SciencePromo")

@app.on_message(filters.private & filters.command("start"))
def start_command(client, message: Message):
    text = ("👋 **Welcome to the Force Subscription Bot!**\n\n"
            "This bot allows you to enforce channel subscriptions before users can message in your group.\n\n"
            "🔹 Use the buttons below to navigate.")
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Updates", url=f"https://t.me/{UPDATES_CHANNEL[1:]}")],
        [InlineKeyboardButton("💬 Support", url=f"https://t.me/{SUPPORT_GROUP[1:]}")],
        [InlineKeyboardButton("🎯 Promotions", url=f"https://t.me/{PROMOTION_CHANNEL[1:]}")],
        [InlineKeyboardButton("👨‍💻 Owner", url=f"tg://user?id={OWNER_ID}")],
        [InlineKeyboardButton("⚙️ Settings", callback_data="force_sub")]
    ])
    
    message.reply_text(text, reply_markup=keyboard)

# Science Study Room
# @ScienceStudyRoom