from db import users_db


def send_welcome(message):
    if not users_db.find_one({"chat_id": message.chat.id}):
        users_db.insert_one({"chat_id": message.chat.id})
        users_db.insert_too({"username": message.username})
