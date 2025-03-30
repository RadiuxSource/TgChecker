# Core module for handling bot functionalities

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
import os

@app.on_message(filters.command("start") & filters.private)
def start_command(client, message: Message):
    text = "👋 Welcome to the Bot! Choose an option below:"
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔹 Use as Force Subscriber", callback_data="force_sub")],
        [InlineKeyboardButton("🔧 Manage Channels", callback_data="manage_channels")]
    ])
    message.reply_text(text, reply_markup=keyboard)

@app.on_callback_query(filters.regex("manage_channels"))
def manage_channels(client, callback_query: CallbackQuery):
    text = "🔧 **Manage Your Channels**\n\nChoose an option:"
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add Channel", callback_data="add_channel")],
        [InlineKeyboardButton("➖ Remove Channel", callback_data="remove_channel")],
        [InlineKeyboardButton("🔙 Back", callback_data="start")]
    ])
    callback_query.message.edit_text(text, reply_markup=keyboard)

# Science Study Room