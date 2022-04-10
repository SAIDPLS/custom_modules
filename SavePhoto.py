import os
from pyrogram import Client, filters
from pyrogram.filters import command, text
from io import BytesIO
from utils.misc import modules_help, prefix





#Скачивание горящих фото
@Client.on_message(filters.command("сф", prefix) & filters.me & filters.reply)
async def download(client: Client, message: types.Message):
    text = message.text[3:]
    media = message.reply_to_message.media
    if not media:
        await message.edit("Реплаем на медиа!")
        return
    await message.edit("С меня конфетка😀")

    path = await message.reply_to_message.download()
    await getattr(client, "send_" + media)("me", path)
    os.remove(path)
    
    modules_help["rl"] = {
    "сф [На медиа]" : "Работает везде"
}
