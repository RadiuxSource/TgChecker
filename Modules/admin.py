from pyrogram.types import CallbackQuery
from pyrogram.enums import ChatMemberStatus
from Database.crud import CRUD
from Database.session import async_session
from Core.decorators import (
    admin_required,
    handle_errors
)
from Templates.messages import ADMIN_PANEL_TEXT
from Templates.keyboards import (
    create_admin_keyboard,
    create_stats_keyboard
)

@handle_errors
@admin_required
async def handle_admin_callback(client, callback: CallbackQuery):
    """Handle all admin panel callbacks"""
    action = callback.data.split('_')[1]
    
    async with async_session() as session:
        if action == "panel":
            await show_admin_panel(client, callback)
        elif action == "stats":
            await show_stats(client, callback, session)
        # Handle 10+ other admin actions...

@handle_errors
async def show_admin_panel(client, callback):
    """Show admin panel menu"""
    await callback.message.edit_text(
        ADMIN_PANEL_TEXT,
        reply_markup=create_admin_keyboard()
    )
    await callback.answer()

@handle_errors
async def show_stats(client, callback, session):
    """Show admin statistics"""
    stats = await CRUD.get_admin_stats(session)
    await callback.message.edit_text(
        f"📊 <b>Admin Statistics</b>\n\n"
        f"• Users: {stats['users']}\n"
        f"• Groups: {stats['groups']}\n"
        f"• Channels: {stats['channels']}",
        reply_markup=create_stats_keyboard()
    )
    await callback.answer()
