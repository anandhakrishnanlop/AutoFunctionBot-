#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from script import script


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    try:
        await message.reply_text(
            text=script.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🧑‍🔬Owner🧑‍🔬", url="https://t.me/AkFrolicx"),
                        InlineKeyboardButton("📽️Updates📽️", url="https://t.me/AkFrolicx_Here"),
                    ],
                    [
                        InlineKeyboardButton(
                            "⚜️ MAIN CHANNELI ⚜️", url="https://t.me/Ssm_Cinemas")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    try:
        await message.reply_text(
            text=script.HELP_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🧑‍🔬Owner🧑‍🔬", url="https://t.me/AkFrolicx"),
                        InlineKeyboardButton("📽️Updates📽️", url="https://t.me/AkFrolicx_Here"),
                    ],
                    [
                        InlineKeyboardButton(
                            "⚜️ Main Channel ⚜️", url="https://t.me/Ssm_Cinemas")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    try:
        await message.reply_text(
            text=script.ABOUT_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🧑‍🔬 Owner 🧑‍🔬", url="https://t.me/AkFrolicx"),
                        InlineKeyboardButton("📽️ Updates 📽️", url="https://t.me/AkFrolicx_Here"),
                    ],
                    [
                        InlineKeyboardButton(
                            "🧿 Creater 🧿", url="https://t.me/AkFrolicx")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass
