from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6195046886:AAGYJkewBHDNYH-jrZu-n6a-8-Wa9DYgvzk')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Open website', web_app=WebAppInfo(url='https://ru.wikibooks.org/wiki/Flask')))
    await message.answer('Hello my friend!', reply_markup=markup)

executor.start_polling(dp)