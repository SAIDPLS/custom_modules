import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from utils.misc import modules_help,  prefix

BASE = "https://hastebin.com"


@Client.on_message(filters.command("haste", prefix) & filters.reply)
def haste(client: Client, message: Message):
    reply = message.reply_to_message

    if reply.text is None:
        return

    message.delete()

    result = requests.post(
        "{}/documents".format(BASE),
        data=reply.text.encode("UTF-8")
    ).json()

    message.reply(
        "{}/{}.py".format(BASE, result["key"]),
        reply_to_message_id=reply.message_id
    )

modules_help["haste"] = {
    "haste" : "reply to text will upload text to hastebin ;)"
}
