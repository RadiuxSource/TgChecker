import pymongo
import os

# Get MongoDB URI from environment variables
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
client = pymongo.MongoClient(MONGO_URI)
db = client["MemberCheckerDB"]  # Database name
users_collection = db["users"]  # Collection for storing user data

def add_user(user_id, username):
    """Adds a user to the database."""
    if not users_collection.find_one({"user_id": user_id}):
        users_collection.insert_one({"user_id": user_id, "username": username})
        return True
    return False

def get_user(user_id):
    """Fetch user data from the database."""
    return users_collection.find_one({"user_id": user_id})
