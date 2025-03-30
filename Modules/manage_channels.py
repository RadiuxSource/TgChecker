from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message

# Dictionary to store required channels per group
required_channels = {}  # {chat_id: [channel1, channel2, ...]}
LOG_GROUP_ID = -1001234567890  # Replace with actual log group ID

@app.on_callback_query(filters.regex("manage_channels"))
def manage_channels(client, callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    
    text = "\n📢 **Manage Your Force Subscription Channels** \n\n"
    text += "You can add or remove the channels that users must join before messaging in your group.\n"
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add Channel", callback_data="add_channel")],
        [InlineKeyboardButton("➖ Remove Channel", callback_data="remove_channel")],
        [InlineKeyboardButton("🔙 Back", callback_data="force_sub")]
    ])
    
    callback_query.message.edit_text(text, reply_markup=keyboard)

@app.on_callback_query(filters.regex("add_channel"))
def add_channel_prompt(client, callback_query: CallbackQuery):
    chat_id = callback_query.from_user.id
    user_status = check_user_status(chat_id)  # Check if user is a member of required channel
    
    if not user_status:
        callback_query.message.edit_text("❌ You must join our federation and add @QuizzoraBot to your group to proceed.")
        return
    
    callback_query.message.edit_text("✏️ Send the channel details in the format:\n\nChannel Name\nChannel Link\nDescription")

@app.on_message(filters.private & filters.text)
def add_channel(client, message: Message):
    chat_id = message.chat.id
    data = message.text.strip().split("\n")
    
    if len(data) < 3:
        message.reply_text("❌ Invalid format! Please send details as:\n\nChannel Name\nChannel Link\nDescription")
        return
    
    channel_name, channel_link, description = data[0], data[1], "\n".join(data[2:])
    
    if chat_id not in required_channels:
        required_channels[chat_id] = []
    
    required_channels[chat_id].append(channel_link)
    message.reply_text(f"✅ Successfully added {channel_name} to your force subscription list!")
    
    # Forward details to log group
    log_message = f"📢 **New Channel Added**\n👤 User: {message.from_user.mention}\n🏷 Name: {channel_name}\n🔗 Link: {channel_link}\n📝 Description: {description}"
    client.send_message(LOG_GROUP_ID, log_message)

@app.on_callback_query(filters.regex("remove_channel"))
def remove_channel_prompt(client, callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    
    if chat_id not in required_channels or not required_channels[chat_id]:
        callback_query.message.edit_text("❌ No channels to remove!")
        return
    
    keyboard = [[InlineKeyboardButton(channel, callback_data=f"remove_{channel}")] for channel in required_channels[chat_id]]
    keyboard.append([InlineKeyboardButton("🔙 Back", callback_data="manage_channels")])
    
    callback_query.message.edit_text("Select a channel to remove:", reply_markup=InlineKeyboardMarkup(keyboard))

@app.on_callback_query(filters.regex("remove_@"))
def remove_channel(client, callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    channel = callback_query.data.replace("remove_", "")
    
    if chat_id in required_channels and channel in required_channels[chat_id]:
        required_channels[chat_id].remove(channel)
        callback_query.message.edit_text(f"✅ Removed {channel} from your force subscription list!")
        
        # Forward removal info to log group
        log_message = f"❌ **Channel Removed**\n👤 User: {callback_query.from_user.mention}\n🏷 Name: {channel}"
        client.send_message(LOG_GROUP_ID, log_message)
    else:
        callback_query.message.edit_text("❌ Channel not found!")

# Function to check if user is a member of the required federation

def check_user_status(user_id):
    # This function should check if the user is part of the required federation channel
    return True  # Placeholder, replace with actual check

#Science Study Room
