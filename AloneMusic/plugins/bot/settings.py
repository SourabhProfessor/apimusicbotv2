#
# Copyright (C) 2021-2022 by TheAloneteam@Github, < https://github.com/TheAloneTeam >.
#
# This file is part of < https://github.com/TheAloneTeam/AloneMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheAloneTeam/AloneMusic/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import CallbackQuery, Message

from AloneMusic import app
from config import BANNED_USERS


@app.on_message(
    filters.command(["settings", "setting"]) & filters.group & ~BANNED_USERS
)
async def settings_mar(client, message: Message):
    return


@app.on_callback_query(
    filters.regex(
        pattern=r"^(settings_helper|bot_info_data|shiv_aarumi|settingsback_helper|SEARCHANSWER|PLAYMODEANSWER|PLAYTYPEANSWER|AUTHANSWER|ANSWERVOMODE|VOTEANSWER|PM|AU|VM|FERRARIUDTI|MODECHANGE|CHANNELMODECHANGE|PLAYTYPECHANGE|AUTH|AUTHLIST|VOMODECHANGE)$"
    )
    & ~BANNED_USERS
)
async def settings_cb(client, CallbackQuery: CallbackQuery):
    try:
        await CallbackQuery.answer()
    except:
        pass
    return
  
