#  Dragon-Userbot - telegram userbot
#  Copyright (C) 2020-present Dragon Userbot Organization
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio
import time

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from utils.misc import modules_help, prefix


@Client.on_message(filters.command(["type","typewriter"] prefix) & filters.me)
async def type_cmd(_, message: Message):
    text = message.text.split(maxsplit=1)[1]
    typed = ""
    typing_symbol = "▒"

    for char in text:
        await message.edit(typed + typing_symbol)
        await asyncio.sleep(0.1)
        typed += char
        await message.edit(typed)
        await asyncio.sleep(0.1)


modules_help["type"] = {
    "type</code> <code>| </code><code>typewriter [text]*": "Typing emulation. Don't use a lot of characters, you can receive a lot of floodwaits!"
}
