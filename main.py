from pyrogram import Client, filters
import datetime

date_time = datetime.datetime.now()
current_time = date_time.time()
print(current_time)

bot = Client(
    api_id=17254355,
    api_hash="f4357abed0b378bf8a8742cb4ecce942",
    bot_token="7289704829:AAHRLha68WX70fBEgL0gjdxp8Na62U1JcPc",
    name='Помощник'
)


@bot.on_message(filters.command('info'))
async def info(client, message):
    await message.reply('Все команды:')
    await message.reply('/start')


@bot.on_message(filters.command('start'))
async def start(client, message):
    await message.reply('Добро пожаловать')


@bot.on_message(filters.text)
async def echo(client, message):
    if message.text.lower() == 'привет':
        await message.reply('Привет')
    elif message.text.lower() == 'пока':
        await message.reply('Пока')
    else:
        await message.reply(f'Ты написал: {message.text}')

bot.run()