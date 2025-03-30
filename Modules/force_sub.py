from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message

# Dictionary to store force subscription channels per group
force_sub_channels = {}  # {chat_id: [channel1, channel2, ...]}
LOG_GROUP_ID = -1001234567890  # Replace with actual log group ID
OWNER_CHANNEL = "@ScienceStudyRoom"  # Replace with your channel

# Maximum free channels per user
MAX_FREE_CHANNELS = 2

@app.on_message(filters.group & ~filters.bot)
def check_subscription(client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    if chat_id not in force_sub_channels:
        return  # No force subscription set for this group
    
    not_subscribed = []
    for channel in force_sub_channels[chat_id]:
        try:
            member = client.get_chat_member(channel, user_id)
            if member.status in ["kicked", "left"]:
                not_subscribed.append(channel)
        except:
            not_subscribed.append(channel)
    
    if not_subscribed:
        warning_text = "🚨 You must join the required channels to send messages here!"
        buttons = [[InlineKeyboardButton("📢 Join Now", url=f"https://t.me/{not_subscribed[0][1:]}")],
                   [InlineKeyboardButton("✅ I've Joined", callback_data="verify_subscription")]]
        message.reply_text(warning_text, reply_markup=InlineKeyboardMarkup(buttons))

@app.on_callback_query(filters.regex("verify_subscription"))
def verify_subscription(client, callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    
    not_subscribed = []
    for channel in force_sub_channels.get(chat_id, []):
        try:
            member = client.get_chat_member(channel, user_id)
            if member.status in ["kicked", "left"]:
                not_subscribed.append(channel)
        except:
            not_subscribed.append(channel)
    
    if not_subscribed:
        callback_query.answer("❌ You haven't joined all required channels!", show_alert=True)
    else:
        callback_query.answer("✅ Verified! You can now send messages.", show_alert=True)
        callback_query.message.delete()

@app.on_callback_query(filters.regex("force_sub"))
def force_sub_menu(client, callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    text = "🔧 **Force Subscription Settings** \n\nSelect an option:"
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add Channel", callback_data="add_channel")],
        [InlineKeyboardButton("➖ Remove Channel", callback_data="remove_channel")],
        [InlineKeyboardButton("💰 Upgrade Subscription", callback_data="upgrade_plan")],
        [InlineKeyboardButton("🔙 Back", callback_data="start")]
    ])
    callback_query.message.edit_text(text, reply_markup=keyboard)

@app.on_callback_query(filters.regex("add_channel"))
def add_channel_prompt(client, callback_query: CallbackQuery):
    chat_id = callback_query.from_user.id
    
    if len(force_sub_channels.get(chat_id, [])) >= MAX_FREE_CHANNELS:
        callback_query.message.edit_text("⚠️ You can only add up to 2 channels for free. Upgrade to add more!")
        return
    
    callback_query.message.edit_text("✏️ Send the channel username (e.g., @ScienceStudyRoom)")

@app.on_callback_query(filters.regex("upgrade_plan"))
def upgrade_plan(client, callback_query: CallbackQuery):
    text = "💰 **Upgrade Plan** \n\nTo add more than 2 channels, you need to purchase a monthly subscription or verify using tokens."
    callback_query.message.edit_text(text)

# Aditya, Aman, Chhotu - Example functions

def aditya_function():
    return "This function is related to Aditya's logic."

def aman_function():
    return "This function is related to Aman's logic."

def chhotu_function():
    return "This function is related to Chhotu's logic."

# Science Study Room
