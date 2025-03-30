from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup
)
from config import Config

def create_main_menu(user_tier: int = 0):
    """Create dynamic main menu based on user tier"""
    buttons = [
        [
            InlineKeyboardButton("🛠 Force Sub Setup", callback_data="force_sub_setup"),
            InlineKeyboardButton("📊 Analytics", callback_data="analytics")
        ]
    ]
    
    if user_tier >= 1:  # Admin
        buttons.append([
            InlineKeyboardButton("👑 Admin Panel", callback_data="admin_panel"),
            InlineKeyboardButton("💎 Premium", callback_data="premium_info")
        ])
    
    buttons.append([
        InlineKeyboardButton("📢 Updates", url=f"t.me/{Config.UPDATE_CHANNEL}"),
        InlineKeyboardButton("💬 Support", url=f"t.me/{Config.SUPPORT_CHAT}")
    ])
    
    return InlineKeyboardMarkup(buttons)

def create_admin_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📈 Stats", callback_data="admin_stats"),
            InlineKeyboardButton("⚙ Settings", callback_data="admin_settings")
        ],
        [
            InlineKeyboardButton("👥 Manage Users", callback_data="admin_users"),
            InlineKeyboardButton("📢 Broadcast", callback_data="admin_broadcast")
        ],
        [
            InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")
        ]
    ])

# 15+ more keyboard templates...
