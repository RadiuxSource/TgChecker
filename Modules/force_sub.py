from pyrogram import filters
from pyrogram.types import Message
from Database.crud import CRUD
from Database.session import async_session
from Templates.messages import (
    WARNING_MESSAGE,
    WELCOME_MESSAGE
)
from Templates.keyboards import (
    create_verification_keyboard,
    create_channel_links
)
from Core.decorators import handle_errors
from Core.utils import delete_message_after

@handle_errors
async def check_member(client, message: Message):
    """Check if user is subscribed to required channels"""
    async with async_session() as session:
        # Get group settings
        group = await CRUD.get_group(session, message.chat.id)
        if not group or not group.force_sub_enabled:
            return

        # Check subscriptions
        unsubscribed = []
        for channel in group.channels:
            if not await CRUD.check_subscription(session, message.from_user.id, channel.channel_id):
                unsubscribed.append(channel.channel)
        
        if unsubscribed:
            await handle_unsubscribed_user(client, message, unsubscribed, group)

@handle_errors
@delete_message_after(30)
async def handle_unsubscribed_user(client, message, channels, group):
    """Handle unsubscribed users with interactive messages"""
    # Delete user's message if enabled
    if group.delete_unsubscribed_messages:
        try:
            await message.delete()
        except:
            pass

    # Prepare message
    text = WARNING_MESSAGE.format(
        user_mention=message.from_user.mention(),
        channel_links="\n".join(create_channel_links(channels))
    )
    
    # Send warning with buttons
    await message.reply_text(
        text,
        reply_markup=create_verification_keyboard(
            user_id=message.from_user.id,
            channels=channels
        ),
        disable_web_page_preview=True
    )
