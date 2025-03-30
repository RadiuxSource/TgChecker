from pyrogram import filters
from pyrogram.types import CallbackQuery, Message
from Database.crud import CRUD
from Database.session import async_session
from Core.decorators import handle_errors, admin_required
from Templates.messages import (
    CHANNEL_ADDED_MSG,
    CHANNEL_REMOVED_MSG
)
from Templates.keyboards import (
    create_channels_menu,
    create_back_button
)

@handle_errors
async def handle_channel_callback(client, callback: CallbackQuery):
    """Handle all channel-related callbacks"""
    action = callback.data.split('_')[1]
    
    async with async_session() as session:
        if action == "add":
            await add_channel(client, callback, session)
        elif action == "remove":
            await remove_channel(client, callback, session)
        elif action == "list":
            await list_channels(client, callback, session)

@admin_required
@handle_errors
async def add_channel(client, callback: CallbackQuery, session):
    """Add a new channel to the system"""
    # Implementation with proper validation
    channel_data = {...}  # Get from callback
    await CRUD.add_channel(session, channel_data)
    await callback.message.edit_text(
        CHANNEL_ADDED_MSG.format(name=channel_data['title']),
        reply_markup=create_back_button("channel_menu")
    )
    await callback.answer()

@admin_required
@handle_errors
async def remove_channel(client, callback: CallbackQuery, session):
    """Remove a channel from the system"""
    channel_id = int(callback.data.split('_')[2])
    channel = await CRUD.get_channel(session, channel_id)
    
    if channel:
        await CRUD.remove_channel(session, channel_id)
        await callback.message.edit_text(
            CHANNEL_REMOVED_MSG.format(name=channel.title),
            reply_markup=create_back_button("channel_menu")
        )
    await callback.answer()

@handle_errors
async def list_channels(client, callback: CallbackQuery, session):
    """List all available channels"""
    channels = await CRUD.get_all_channels(session)
    await callback.message.edit_text(
        "📡 Available Channels:\n\n" + 
        "\n".join(f"• {ch.title} (@{ch.username})" for ch in channels),
        reply_markup=create_channels_menu(channels)
    )
    await callback.answer()
