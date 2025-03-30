Here's an updated **README.md** file with a **GitHub description** for your bot:  

---

## **Telegram Member Checker Bot** 🚀  
A powerful **Force Subscription** bot for Telegram channels and groups, built using **Pyrogram**.  
This bot ensures that users **must join specific channels** before they can send messages in a group.  

### **✨ Features:**  
✅ **Force Subscription** – Users must join selected channels before messaging.  
✅ **Custom Channel Management** – Group owners can add/remove channels easily.  
✅ **Limit-Free Usage** – Add up to **2 channels for free** (upgrade for more).  
✅ **Automatic Verification** – Checks whether users are subscribed.  
✅ **Private Messaging** – Guides users in personal chat for better interaction.  
✅ **Auto-Delete Warnings** – Configurable timers to auto-delete warning messages.  
✅ **Secure & Scalable** – Uses **MongoDB** for database storage.  

---

## **🔧 Deployment Instructions**  
### **1️⃣ Installation**  
Make sure you have **Python 3.10+** installed. Then, clone the repository and install dependencies:  

```bash
git clone https://github.com/yourusername/Telegram-Member-Checker-Bot.git  
cd Telegram-Member-Checker-Bot  
pip install -r requirements.txt  
```

---

### **2️⃣ Setup Environment Variables**  
Create a `.env` file in the root folder and fill in your bot credentials:  

```ini
API_ID=your_api_id  
API_HASH=your_api_hash  
BOT_TOKEN=your_bot_token  
MONGO_URI=your_mongodb_uri  
OWNER_ID=your_telegram_id  
LOG_GROUP_ID=-1001234567890  
OWNER_CHANNEL=@YourOwnerChannel  
QUIZZORA_BOT=@QuizzoraBot  
```

---

### **3️⃣ Run the Bot**  
Start the bot using:  
```bash
python3 main.py  
```

---

## **📡 Deployment on Koyeb**  
1. **Push your code** to GitHub.  
2. **Go to Koyeb**, create a new service, and connect your GitHub repo.  
3. Set environment variables in **Koyeb Secrets**.  
4. Deploy and enjoy! 🚀  

---

## **📌 Notes**  
- **For support**, contact us at [@ScienceStudyRoom](https://t.me/ScienceStudyRoom).  
- Developed by **Aditya, Aman, and Chhotu** for the **JEE Study Room** project.  

---

Let me know if you want any modifications! 🚀