from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import emoji

inline_kb_start_quest = InlineKeyboardMarkup([
        [InlineKeyboardButton('Пройти квест',
                            callback_date='start_quest')]
    ])
inline_kb_choice_door = InlineKeyboardMarkup([
          [InlineKeyboardButton('левая дверь', callback_data='left_door')],
          [InlineKeyboardButton('правая дверь', callback_data='right_door')]
])

inline_kb_left_door = InlineKeyboardMarkup([
            [InlineKeyboardButton('Сражение с драконом', callback_data='dragon')],
            [InlineKeyboardButton('Попытатся убежать', callback_data='run')]
])
inline_kb_right_door = InlineKeyboardMarkup([
    [InlineKeyboardButton('Золотая корона', callback_data='gold_crow')],
    [InlineKeyboardButton("Серебреный кинжал", callback_data="silver_dagger")],
    [InlineKeyboardButton('Старая книга', callback_data='old_book')]
])


btn_info = KeyboardButton(f'{emoji.INFORMATION} Инфо')
btn_games = KeyboardButton(f'{emoji.VIDEO_GAME} Игры')
btn_profile = KeyboardButton(f'{emoji.PERSON} Профиль')
btn_time = KeyboardButton(f'{emoji.ALARM_CLOCK} Время')
btn_rps = KeyboardButton(f'{emoji.ROLLED_UP_NEWSPAPER} Камень ножницы бумага')
btn_menu = KeyboardButton(f'{emoji.BACK_ARROW} Назад')
btn_quest = KeyboardButton(f'{emoji.RED_QUESTION_MARK} Квест')
btn_rock = KeyboardButton(f'{emoji.ROCK} Камени')
btn_scissors = KeyboardButton(f'{emoji.SCISSORS} Ножницы')
btn_paper = KeyboardButton(f'{emoji.ROLL_OF_PAPER} Бумага')
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