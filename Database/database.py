import os
from motor.motor_asyncio import AsyncIOMotorClient

# Fetch MongoDB URL from environment variables
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

# Initialize MongoDB Client
client = AsyncIOMotorClient(MONGO_URL)
db = client.get_database("TgChecker")

# Collections
groups_collection = db.get_collection("groups")
users_collection = db.get_collection("users")
channels_collection = db.get_collection("channels")
subscriptions_collection = db.get_collection("subscriptions")

def get_user(user_id: int):
    return users_collection.find_one({"user_id": user_id})

def add_user(user_id: int, username: str):
    return users_collection.update_one(
        {"user_id": user_id},
        {"$set": {"username": username}},
        upsert=True
    )

def get_group(group_id: int):
    return groups_collection.find_one({"group_id": group_id})

def add_group(group_id: int, title: str):
    return groups_collection.update_one(
        {"group_id": group_id},
        {"$set": {"title": title}},
        upsert=True
    )

def get_channels(owner_id: int):
    return channels_collection.find({"owner_id": owner_id})

def add_channel(owner_id: int, channel_username: str, description: str):
    return channels_collection.insert_one({
        "owner_id": owner_id,
        "channel_username": channel_username,
        "description": description
    })

def remove_channel(owner_id: int, channel_username: str):
    return channels_collection.delete_one({
        "owner_id": owner_id, "channel_username": channel_username
    })

# Science Study Room