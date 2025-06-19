from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["todoApp"]
users = db["users"]

# 🧠 Get user's tasks
def get_tasks(username):
    user = users.find_one({"username": username})
    return user["tasks"] if user else []

# ➕ Add new task
def add_task(username, title):
    users.update_one(
        {"username": username},
        {"$push": {"tasks": {"title": title, "done": False}}}
    )

# 🔁 Toggle task status
def toggle_task(username, index):
    user = users.find_one({"username": username})
    if not user: return
    tasks = user["tasks"]
    if 0 <= index < len(tasks):
        tasks[index]["done"] = not tasks[index]["done"]
        users.update_one({"username": username}, {"$set": {"tasks": tasks}})

# ❌ Delete task
def delete_task(username, index):
    user = users.find_one({"username": username})
    if not user: return
    tasks = user["tasks"]
    if 0 <= index < len(tasks):
        del tasks[index]
        users.update_one({"username": username}, {"$set": {"tasks": tasks}})
