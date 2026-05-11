from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")

db = client["chatup_ai"]

users = db["users"]
messages = db["messages"]
activity = db["activity"]
connections = db["connections"]

# ---------------- LOG ACTIVITY ----------------
def log_activity(username, action):

    activity.insert_one({
        "username": username,
        "action": action,
        "timestamp": datetime.utcnow()
    })

# ---------------- SAVE MESSAGE ----------------
def save_message(sender, receiver, message, msg_type):

    messages.insert_one({
        "sender": sender,
        "receiver": receiver,
        "message": message,
        "type": msg_type,
        "timestamp": datetime.utcnow()
    })
