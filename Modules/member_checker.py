from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
import config
from Core.logger import logger

# List of channels the bot will check
CHANNELS = ["@your_channel_username"]  # Replace with your actual channel

@Client.on_message(filters.command("check"))
async def check_membership(client, message):
    user_id = message.from_user.id
    username = message.from_user.username or "No Username"

    for channel in CHANNELS:
        try:
            member = await client.get_chat_member(channel, user_id)
            if member.status in ["member", "administrator", "creator"]:
                await message.reply_text(f"✅ You are a member of {channel}.")
            else:
                await message.reply_text(f"❌ You are not a member of {channel}. Please join and try again.")
        except UserNotParticipant:
            await message.reply_text(f"❌ You are not a member of {channel}. Please join and try again.")
        except Exception as e:
            logger.error(f"Error checking membership: {e}")
            await message.reply_text("⚠️ An error occurred while checking your membership.")

    logger.info(f"Membership check done for {username} ({user_id})")
