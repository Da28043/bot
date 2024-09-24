from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup
from pyrogram import emoji

btn_info = KeyboardButton(f'{emoji.INFORMATION} Инфо')
btn_games = KeyboardButton(f'{emoji.VIDEO_GAME} Игры')
btn_profile = KeyboardButton(f'{emoji.PERSON} Профиль')
btn_time = KeyboardButton(f'{emoji.ALARM_CLOCK} Время')

kb_main = ReplyKeyboardMarkup(
    keyboard=[
                [btn_info, btn_games, btn_profile, btn_time]
    ],
    resize_keyboard=True
)