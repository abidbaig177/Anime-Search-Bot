from pyrogram.types import Message
from pyrogram import filters
from AniPlay import app
from AniPlay.plugins.AnimeDex import AnimeDex
from AniPlay.plugins.button import BTN
from AniPlay.plugins.db import get_all_users, is_user_in_db, save_user_in_db


async def isUserJoined(user):
    try:
        chat = await app.get_chat_member("Anime_Pirates", user)
        return True
    except:
        return False


async def broadcast_message(message: Message):
    users = get_all_users()
    x = await message.reply_text(f"Broadcasting to {len(users)} users...")
    for user in users:
        try:
            await message.reply_to_message.forward(user)
        except:
            pass
    await x.reply_text("Broadcast Completed...")


@app.on_message(filters.command(["start", "ping", "help", "alive"]))
async def start(_, message: Message):
    if not is_user_in_db(message.from_user.id):
        save_user_in_db(message.from_user.id)

    if not await isUserJoined(message.from_user.id):
        return await message.reply_text("Join @Anime_Pirates to use this bot...")
    try:
        await message.reply_text(
            "Bot Is Online...\nSearch Animes Using /search or /s\n\n Join - @Anime_Pirates @Ongoing_Animes_Hats for More..."
        )
    except:
        return


QUERY = "**Search Results:** `{}`"


@app.on_message(filters.command(["search", "s"]))
async def searchCMD(_, message: Message):
    if not is_user_in_db(message.from_user.id):
        save_user_in_db(message.from_user.id)

    if not await isUserJoined(message.from_user.id):
        return await message.reply_text("Join @Anime_Pirates to use this bot...")
    try:
        user = message.from_user.id
        query = " ".join(message.command[1:])
        if query == "":
            return await message.reply_text("Give me something to search ^_^")
        data = AnimeDex.search(query)
        button = BTN.searchCMD(user, data, query)
        await message.reply_text(QUERY.format(query), reply_markup=button)
    except Exception as e:
        try:
            return await message.reply_text(
                "**Anime Not Found...**\n\nProbably Incorrect Name, Try again"
            )
        except:
            return


@app.on_message(
    filters.command("broadcast")
    & filters.user(1891736799)
    & filters.private
    & filters.incoming
)
async def broadcast(_, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a message to broadcast...")

    await broadcast_message(message)
