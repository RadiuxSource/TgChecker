from datetime import datetime, timedelta
from pyrogram.types import CallbackQuery
from Database.crud import CRUD
from Database.session import async_session
from Core.decorators import handle_errors, admin_required
from Core.utils import format_time
from Templates.keyboards import create_analytics_keyboard

@handle_errors
async def handle_analytics(client, callback: CallbackQuery):
    """Handle analytics dashboard"""
    time_range = callback.data.split('_')[1] if '_' in callback.data else 'week'
    
    async with async_session() as session:
        stats = await CRUD.get_analytics(session, time_range)
        
        text = f"📊 *Analytics* ({time_range.capitalize()})\n\n"
        text += f"• New Users: `{stats['new_users']}`\n"
        text += f"• Active Groups: `{stats['active_groups']}`\n"
        text += f"• Messages Processed: `{stats['messages']}`\n"
        text += f"• Subscription Rate: `{stats['sub_rate']}%`\n\n"
        text += f"🔄 Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        
        await callback.message.edit_text(
            text,
            reply_markup=create_analytics_keyboard(time_range)
        )
    await callback.answer()
