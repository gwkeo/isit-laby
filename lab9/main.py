import telebot
from telebot import types

token = ''

bot = telebot.TeleBot(token)
count = 0

def markup(c):
    c = int(c)
    keyboard = types.InlineKeyboardMarkup()
    up_button = types.InlineKeyboardButton(text="Мне нравится", callback_data=f"up:{c+1}")
    down_button = types.InlineKeyboardButton(text="Мне не нравится", callback_data=f"down:{c-1}")
    keyboard.add(up_button, down_button)
    return keyboard

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id=message.chat.id, text=f"Число нажатий: {count}", reply_markup=markup(count))

@bot.callback_query_handler()
def callback_handler(callback):
    message_id = callback.message.message_id
    c = callback.data.split(':')[1]
    match callback.data.split(':')[0]:
        case "up":
            bot.edit_message_text(chat_id=callback.message.chat.id, text=f"Число нажатий: {c}", message_id=message_id, reply_markup=markup(c))
        case "down":
            bot.edit_message_text(chat_id=callback.message.chat.id, text=f"Число нажатий: {c}", message_id=message_id, reply_markup=markup(c))

bot.infinity_polling()