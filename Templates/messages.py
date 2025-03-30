from config import Config

# Welcome messages
WELCOME_MESSAGE = """
✨ *Welcome to {bot_name}!* ✨

🔹 **What I can do:**
- Enforce channel subscriptions
- Manage group members
- Provide analytics
- Premium features

📌 Join our channel: @{update_channel}
""".format(
    bot_name="Force Sub Bot",
    update_channel=Config.UPDATE_CHANNEL
)

WARNING_MESSAGE = """
⚠️ *Subscription Required* ⚠️

Dear {user_mention},

You need to join these channels to continue:

{channel_links}

👉 After joining, click below to verify:
"""

# Admin messages
ADMIN_PANEL_TEXT = """
🛠 *Admin Control Panel*

• Users: `{user_count}`
• Groups: `{group_count}`
• Channels: `{channel_count}`

Choose an action below:
"""

LOG_TEMPLATE = """
[{timestamp}] {level}:
{message}
"""

# Payment messages
PAYMENT_PROMPT = """
💎 *Premium Subscription*

🔹 Benefits:
- Unlimited channels
- Priority support
- Advanced analytics

💰 Price: ${price}/month
🔄 Billed monthly

Click below to subscribe:
"""

# 15+ more professionally designed message templates...
