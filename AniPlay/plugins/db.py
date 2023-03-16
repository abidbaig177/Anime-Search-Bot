import pymongo
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://Animepirates:ULTRA123@cluster0.dv9jlez.mongodb.net/?retryWrites=true&w=majority"
)
db = client["AniPlay"]
collection = db["users"]


def save_user_in_db(user_id):
    try:
        if not collection.find_one({"user_id": user_id}):
            collection.insert_one({"user_id": user_id})
        print("User Saved In DB :", user_id)
    except Exception as e:
        print(e)


def is_user_in_db(user_id):
    try:
        if collection.find_one({"user_id": user_id}):
            return True
        else:
            return False
    except Exception as e:
        print(e)


def get_all_users():
    try:
        x = collection.find()
        users = []
        for i in x:
            users.append(i["user_id"])
        return users
    except Exception as e:
        print(e)
