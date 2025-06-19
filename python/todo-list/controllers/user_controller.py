import random
import string
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import bcrypt

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["todoApp"]
users = db["users"]

def create_user(username, password):
    existing = users.find_one({"username": username})
    if existing:
        return "❌ Username already exists"

    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    new_user = {
        "username": username,
        "password": hashed_pw.decode(),  # Store as string
        "tasks": []
    }
    users.insert_one(new_user)
    return {"success": True, "message": "✅ User registered successfully"}



def login_user(username, password):
    user = users.find_one({"username": username})
    if not user:
        return {"success": False, "message": "❌ User not found"}

    if bcrypt.checkpw(password.encode(), user["password"].encode()):
        return {"success": True, "message": "✅ Login successful", "user": user["username"]}

    return {"success": False, "message": "❌ Incorrect password"}


def suggest_username():
    adjectives = ["smart", "brave", "cool", "fast", "silent", "sharp", "coded", "lazy", "dev", "neo"]
    nouns = ["tiger", "ninja", "wolf", "falcon", "coder", "hacker", "matrix", "wizard", "ai", "bot"]

    while True:
        name = f"{random.choice(adjectives)}_{random.choice(nouns)}_{random.randint(10, 99)}"
        if not users.find_one({"username": name}):
            return name