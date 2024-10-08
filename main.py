import json
import random

from pyrogram import Client, filters
from random import randint
import datetime
import keyboards

date_time = datetime.datetime.now()
current_time = date_time.time()


bot = Client(
    api_id=17254355,
    api_hash="f4357abed0b378bf8a8742cb4ecce942",
    bot_token="7289704829:AAHRLha68WX70fBEgL0gjdxp8Na62U1JcPc",
    name='Помощник'
)

def button_filter(button):
   async def func(_, __, msg,):
       return msg.text == button.text
   return filters.create(func, "ButtonFilter", button=button)

@bot.on_message(filters.command('info') | button_filter(keyboards.btn_info))
async def info(client, message):
    await message.reply('Все команды:')
    await message.reply('/start')
    await message.reply('/time')
    await message.reply('/game')
    await message.reply('/profile')
    await message.reply('/quest')
@bot.on_message(filters.command('time'))
async def time(client, message):
    date_time = datetime.datetime.now()
    current_time = date_time.time()
    await message.reply(f'Текущее время -{current_time}')
@bot.on_message(filters.command('profile') | button_filter(keyboards.btn_profile))
async def profile(client, message):
    with open("users.json", "r") as file:
        users = json.load(file)
    id=message.from_user.id
    await message.reply(f'Текущие очики - {users[str(id)]}')

@bot.on_message(filters.command('game') | button_filter(keyboards.btn_games))
async def game(client, messege):
    with open("users.json", "r") as file:
        users = json.load(file)
    if users[str(messege.from_user.id)] >= 5:
        await messege.reply("Выберите игру",
                            reply_markup=keyboards.kb_games
                            )
    else:
        await messege.reply(f"Не хватает средств. На твоём счету{users[str(messege.from_user.id)]} Минимальная сумма для игры - 5")

@bot.on_message(filters.command('rps') | button_filter(keyboards.btn_rps))
async def rps(bot, messege):
    await messege.reply("Твой ход", reply_markup=keyboards.kb_rps
                        )
# @bot.on_message(button_filter(keyboards.btn_rock), (keyboards.btn_scissors), (keyboards.btn_scissors)) |
#                 # button_filter(keyboards.btn_scissors |
#                 # button_filter(keyboards.btn_paper) )
@bot.on_message(button_filter(keyboards.btn_rock)| button_filter(keyboards.btn_paper)| button_filter(keyboards.btn_scissors))
async def choice_rps(bot, message):
    with open("users.json", "r") as file:
        users = json.load(file)
    rock = keyboards.btn_rock.text
    scissors = keyboards.btn_scissors.text
    paper = keyboards.btn_paper.text
    user = message.text
    pc = random.choice([rock, scissors, paper])
    print(user, pc)
    if user == pc:
        await message.reply('Ничья')
    elif (user == rock and pc == scissors) or (user == scissors and pc == paper) or (
            user == paper and pc == rock):
        await message.reply(f'Ты выйграл. Бот выбрал {pc}',
                            reply_markup=keyboards.kb_games)
        users[str(message.from_user.id)] += 10
    else:
        await message.reply(f"Ты проиграл. Бот выбрал {pc}",
                            reply_markup = keyboards.kb_games)
        users[str(message.from_user.id)] -= 10
    with open("users.json", 'w') as file:
        json.dump(users, file)



@bot.on_message(filters.command('start') | button_filter(keyboards.btn_menu))
async def start(client, message):
    # await message.reply('Добро пожаловать, меня зовут помошник')
    await message.reply("Добро пожаловать!",
                        reply_markup=keyboards.kb_main
                        )
    with open("users.json", "r") as file:
        users = json.load(file)
    if str(message.from_user.id) not in users.keys():
        users[message.from_user.id] = 100
        with open("users.json", "w") as file:
            json.dump(users, file)


# @bot.on_message(filters.text)
# async def echo(client, message):
#     print(message)
#     if message.text.lower() == 'привет':
#         await message.reply('Привет')
#     elif message.text.lower() == 'пока':
#         await message.reply('Пока')
#     elif message.text.lower() == 'как дела?' or message.text.lower() == 'как дела':
#         await message.reply('Нормально')
#     # else:
#     #     await message.reply(f'Ты написал: {message.text}')


#Кнопка для квеста
@bot.on_message(filters.command('quest') | button_filter(keyboards.btn_quest))
async def kvest(bot, message):
    await message.reply_text('Хотите ли вы отправится в увлекательное путешествие,полное приключений и загадок',
                             reply_markup=keyboards.inline_kb_start_quest)

@bot.on_callback_query()
async def handle_query(bot, query):
    await query.message.delete()
    if query.data == 'start_quest':
        await bot.answer_callback_query(query.id,
            text= 'Добро пожаловать в квест под названием Поиски Затереного Сокровища!',
            show_alert=True)
        await query.message.reply_text('Ты стоишь перед двумя дверьми какую из них выберишь?',
                                       reply_markup=keyboards.inline_kb_choice_door)
    elif query.data == 'left_door':
        await query.message.reply_text('Ты входишь в комнату и видишь злого дракона! У тебя есть два варианта действия',
                                       reply_markup=keyboards.inline_kb_left_door)
    elif query.data == 'right_door':
        await query.message.reply_text('Ты входишь в комнату, наполненую сокровищами! Тебе нужно выбрать только одно сокровище',
                                       reply_markup=keyboards.inline_kb_right_door)
    elif query.data == 'dragon':
        await bot.answer_callback_query(query.id, text='Ты сражаешься с драконом но он оказывается слишком сильным. Ты погибаешь',
                                        show_alert=True)
    elif query.data == 'run':
        await bot.answer_callback_query(query.id, text='Ты пытаешься убежать, но дракон догоняет тебя и съедает',
                                        show_alert=True)
    elif query.data =='gold_crown':
        await bot.answer_callback_query(query.id, text='Ты берёшь золотую корону и выходишь из комнаты. Поздравляю! Ты выиграл игру.',
                                        show_alert=True)
    elif query.data == 'silver_dagger':
        await bot.answer_callback_query(query.id, text='Ты берешь серебренный кинжал и выходишь из комнаты. К сожалению, клинок ничего не стоит',
                                        show_alert=True)
    elif query.data == 'old_book':
        await bot.answer_callback_query(query.id, text='Ты берешь старую книгу и выходишь из комнаты. Книга оказывается магической! Ты открываешь страницу и исчезаешь',
                                        show_alert=True)
bot.run()