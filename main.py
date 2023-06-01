import webbrowser

import telebot
from telebot import types

token = '6195046886:AAGYJkewBHDNYH-jrZu-n6a-8-Wa9DYgvzk'
bot = telebot.TeleBot(token)

# Обробка вхідних даних, у прикладі вивід тексту якщо клієнт присилає фото
@bot.message_handler(content_types=['photo', 'audio'])
def get_photo(message):
    #Додавання кнопок
    markup = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton('Go to website', url='http://chat.openai.com/?model=text-davinci-002-render-sha')
    markup.row(button_1)
    button_2 = types.InlineKeyboardButton('Delete photo', callback_data='delete')
    button_3 = types.InlineKeyboardButton('Edit photo', callback_data='edit')
    markup.row(button_2, button_3)

    bot.reply_to(message, 'Very nice photo', reply_markup=markup)




# Відправка користувача на сайт по команді /site або /website
@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://chat.openai.com/?model=text-davinci-002-render-sha')


# По командам вивід привітання з іменем користувача
@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}')


# По командам вивід привітання з додаванням html розмітки текста
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')


# Відповідь по звичайному тексту користувача, не можна ставити на початок цю функці.ю бо не спрацьовують інші команди
# так як message_handler пустий
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)
