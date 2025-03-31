import telebot
from telebot import types

token = ''

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.chat.id, "Привет, мир!")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['живое', 'неживое']])
    msg = bot.send_message(message.chat.id, 'Что выбираешь?', reply_markup=keyboard)

@bot.message_handler()
def name(m):
    if m.text == 'живое':
        bot.send_message(m.chat.id, 'вы выбрали живое')
    else:
        bot.send_message(m.chat.id, 'вы выбрали неживое')

bot.polling(none_stop=True)