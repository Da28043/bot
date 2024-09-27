from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup
from pyrogram import emoji

btn_info = KeyboardButton(f'{emoji.INFORMATION} Инфо')
btn_games = KeyboardButton(f'{emoji.VIDEO_GAME} Игры')
btn_profile = KeyboardButton(f'{emoji.PERSON} Профиль')
btn_time = KeyboardButton(f'{emoji.ALARM_CLOCK} Время')
btn_rps = KeyboardButton(f'{emoji.ROLLED_UP_NEWSPAPER} Камень ножницы бумага')
btn_menu = KeyboardButton(f'{emoji.BACK_ARROW} Назад')
btn_quest = KeyboardButton(f'{emoji.RED_QUESTION_MARK} Квест')
btn_rock = KeyboardButton(f'{emoji.ROCK} Камени')
btn_scissors = KeyboardButton(f'{emoji.SCISSORS} Ножницы')
btn_paper = KeyboardButton(f'{emoji.NOTEBOOK} Камень')
kb_main = ReplyKeyboardMarkup(
    keyboard=[
                [btn_info, btn_games, btn_profile, btn_time]
    ],
    resize_keyboard=True
)
kb_games = ReplyKeyboardMarkup(
    keyboard=[
                [btn_rps, btn_menu, btn_quest]
    ],
    resize_keyboard=True
)
kb_rps = ReplyKeyboardMarkup(
    keyboard=[
                [btn_rock, btn_scissors, btn_paper]
    ],
    resize_keyboard=True
)
