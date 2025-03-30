from functools import wraps
from pyrogram.types import CallbackQuery, Message
from pyrogram.errors import BadRequest
from Database.crud import CRUD
from Database.session import async_session
from Core.utils import send_log

def handle_errors(func):
    """Handle errors gracefully with logging"""
    @wraps(func)
    async def wrapper(client, update, *args, **kwargs):
        try:
            return await func(client, update, *args, **kwargs)
        except BadRequest as e:
            await send_log(f"BadRequest in {func.__name__}: {str(e)}")
        except Exception as e:
            await send_log(f"Error in {func.__name__}: {str(e)}", level="ERROR")
            if isinstance(update, (CallbackQuery, Message)):
                try:
                    await update.reply_text("❌ An error occurred. Please try again later.")
                except:
                    pass
    return wrapper

def admin_required(func):
    """Check if user is admin before executing"""
    @wraps(func)
    async def wrapper(client, update, *args, **kwargs):
        user_id = update.from_user.id
        async with async_session() as session:
            user = await CRUD.get_user(session, user_id)
            if user and user.is_admin:
                return await func(client, update, *args, **kwargs)
        
        if isinstance(update, CallbackQuery):
            await update.answer("🔒 Admin access required!", show_alert=True)
        elif isinstance(update, Message):
            await update.reply_text("🔒 You need admin privileges for this action.")
    return wrapper

def delete_message_after(seconds: int):
    """Delete message after specified time"""
    def decorator(func):
        @wraps(func)
        async def wrapper(client, update, *args, **kwargs):
            result = await func(client, update, *args, **kwargs)
            if isinstance(update, Message):
                await asyncio.sleep(seconds)
                try:
                    await update.delete()
                except:
                    pass
            return result
        return wrapper
    return decorator
