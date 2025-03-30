import stripe
from pyrogram.types import CallbackQuery
from config import Config
from Database.crud import CRUD
from Database.session import async_session
from Core.decorators import handle_errors
from Templates.messages import (
    PAYMENT_PROMPT,
    PAYMENT_SUCCESS_MSG
)
from Templates.keyboards import (
    create_payment_button,
    create_payment_methods_keyboard
)

stripe.api_key = Config.STRIPE_SECRET

@handle_errors
async def handle_payment_callback(client, callback: CallbackQuery):
    """Handle all payment-related callbacks"""
    action = callback.data.split('_')[1]
    
    if action == "subscribe":
        await show_payment_options(client, callback)
    elif action == "stripe":
        await process_stripe_payment(client, callback)
    # Add more payment providers

async def show_payment_options(client, callback: CallbackQuery):
    """Show available payment methods"""
    await callback.message.edit_text(
        PAYMENT_PROMPT.format(price="5"),
        reply_markup=create_payment_methods_keyboard(),
        disable_web_page_preview=True
    )
    await callback.answer()

async def process_stripe_payment(client, callback: CallbackQuery):
    """Process Stripe payment"""
    async with async_session() as session:
        user = await CRUD.get_user(session, callback.from_user.id)
        if not user:
            return await callback.answer("User not found!", show_alert=True)
        
        # Create Stripe checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': Config.STRIPE_PRICE_ID,
                'quantity': 1,
            }],
            mode='subscription',
            success_url=Config.PAYMENT_SUCCESS_URL,
            cancel_url=Config.PAYMENT_CANCEL_URL,
            customer_email=user.email,
            client_reference_id=str(user.user_id)
        )
        
        await callback.message.edit_text(
            "💳 Please complete your payment on:",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Pay with Stripe", url=session.url)
            ]])
        )
        await callback.answer()
