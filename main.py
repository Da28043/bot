from pyrogram import Client, filters
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

@bot.on_message(filters.command('time'))
async def time(client, message):
    date_time = datetime.datetime.now()
    current_time = date_time.time()
    await message.reply(f'Текущее время -{current_time}')

@bot.on_message(filters.command('game') | button_filter(keyboards.btn_games))
async def game(client, messege):
    await messege.reply("Выберите игру")

@bot.on_message(filters.command('start'))
async def start(client, message):
    # await message.reply('Добро пожаловать, меня зовут помошник')
    await message.reply("Добро пожаловать!",
                        reply_markup=keyboards.kb_main
                        )



@bot.on_message(filters.text)
async def echo(client, message):
    print(message)
    if message.text.lower() == 'привет':
        await message.reply('Привет')
    elif message.text.lower() == 'пока':
        await message.reply('Пока')
    elif message.text.lower() == 'как дела?' or message.text.lower() == 'как дела':
        await message.reply('Нормально')
    else:
        await message.reply(f'Ты написал: {message.text}')

bot.run()