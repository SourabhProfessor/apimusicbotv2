#
# Copyright (C) 2021-2022 by TheAloneteam@Github, < https://github.com/TheAloneTeam >.
# This file is part of < https://github.com/TheAloneTeam/AloneMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheAloneTeam/AloneMusic/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

import config
from AloneMusic import app
from AloneMusic.misc import _boot_
from AloneMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
)
from AloneMusic.utils.decorators.language import LanguageStart
from config import BANNED_USERS


@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    # Personal chat mein /start karne par kuch bhi send nahi hoga (Silent)
    return


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    # Group mein /start karne par kuch bhi send nahi hoga (Silent)
    await add_served_chat(message.chat.id)
    return


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    return await app.leave_chat(message.chat.id)

                # Bot jab group mein add hoga tab bhi koi message nahi bhejega, sirf chat save karega
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
