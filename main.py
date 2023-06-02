import webbrowser

import telebot
from telebot import types

token = '6195046886:AAGYJkewBHDNYH-jrZu-n6a-8-Wa9DYgvzk'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    #Додавання кнопок як значків
    markup = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton('Go to website 🫡')   #Ставиш ємодзі в телеграмі, виділяєш, копіюєш і вставляєш сюди
    markup.row(button_1)
    button_2 = types.KeyboardButton('Delete photo')
    button_3 = types.KeyboardButton('Edit photo')
    markup.row(button_2, button_3)
    file = open('./photo.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)   #Відправка фото при старті з виводом кнопок
    # bot.send_audio(message.chat.id, file, reply_markup=markup)  #Відправка аудіо при старті з виводом кнопок
    # bot.send_video(message.chat.id, file, reply_markup=markup)  #Відправка відео при старті з виводом кнопок
    # bot.send_message(message.chat.id, 'Hello', reply_markup=markup)  #Відправка текста при старті з виводом кнопок


#Реєструємо наступну дію після старту, буде спрацьовувати на 1-не нажаття кнопки
    bot.register_next_step_handler(message, on_click)

# Пишемо що буде при нажатті кнопки, в прикладі виводим текст
def on_click(message):
    if message.text == 'Go to website':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Delete photo':
        bot.send_message(message.chat.id, 'Delete')

# Обробка вхідних даних, у прикладі вивід тексту якщо клієнт присилає фото
@bot.message_handler(content_types=['photo', 'audio'])
def get_photo(message):
    #Додавання кнопок. Формування рядка кнопок markup.row, автоматично додати кнопку буде 1 в рядок  markup.add
    markup = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton('Go to website', url='http://chat.openai.com/?model=text-davinci-002-render-sha')
    markup.row(button_1)
    button_2 = types.InlineKeyboardButton('Delete photo', callback_data='delete')
    button_3 = types.InlineKeyboardButton('Edit photo', callback_data='edit')
    markup.row(button_2, button_3)

    bot.reply_to(message, 'Very nice photo', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


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
