from os import environ
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id= int(environ.get("APP_ID", "13296527"),
    api_hash= environ.get("API_HASH", "6ff44fffc149a6dc599a5d2eaeb8873c"),
    bot_token= environ.get("TOKEN", "5929272282:AAEizV80hIdIfhX1dDCvmuW6b7E0qeOVAeE")
)
