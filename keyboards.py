from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup
from pyrogram import emoji

btn_info = KeyboardButton(f'{emoji.INFORMATION} Инфо')
btn_games = KeyboardButton(f'{emoji.VIDEO_GAME} Игры')
btn_profile = KeyboardButton(f'{emoji.PERSON} Профиль')
btn_time = KeyboardButton(f'{emoji.ALARM_CLOCK} Время')
btn_casino = KeyboardButton(f'{emoji.ROLLED_UP_NEWSPAPER} Камень ножницы бумага')
btn_menu = KeyboardButton(f'{emoji.BACK_ARROW} Назад')
btn_quest = KeyboardButton(f'{emoji.RED_QUESTION_MARK} Квест')
kb_main = ReplyKeyboardMarkup(
    keyboard=[
                [btn_info, btn_games, btn_profile, btn_time]
    ],
    resize_keyboard=True
)
kb_games = ReplyKeyboardMarkup(
    keyboard=[
                [btn_casino, btn_menu, btn_quest]
    ],
    resize_keyboard=True
)