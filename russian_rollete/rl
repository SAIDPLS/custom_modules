from pyrogram import Client, filters, types,errors
from pyrogram.filters import command, text
import time
from time import sleep
import random
from utils.misc import modules_help, prefix

#Русская рулетка
@Client.on_message(filters.command("rl", prefix) & filters.me)
async def rr(_, message):
    a = random.randint(0,6)
    user_digit = message.text[4:]
    if int(user_digit) > 6:
     await message.edit("Так нельзя! В револьвере столько патронов нету. Число от 1 до 6")
     return
    await message.edit("Кручу барабан💅...")
    sleep(5)
    if int(user_digit) > a:
        await message.edit("Мои поздравления,ты выжил")
    elif int(user_digit) < a:
        await message.edit("Мои поздравления,ты выжил")
    elif int(user_digit) == a:
        await message.edit("К сожалению вы мертвы")
        
modules_help["rl"] = {
    "rl [число 1-6]" : "Работает везде"
}
