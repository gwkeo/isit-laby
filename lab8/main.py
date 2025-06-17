import telebot
from telebot import types

count = 0

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['аа', 'аб', 'ба', 'бб']])    
    bot.send_message(message.chat.id, f"а! для отображения числа нажатий исопльзуйте команду /count", reply_markup=keyboard)

@bot.message_handler(commands=['count'])
def show_count(message):
    global count
    bot.send_message(chat_id=message.chat.id, text=f"Число нажатий: {count}")

@bot.message_handler()
def msg(message):
    global count
    count += 1
    match(message.text):
        case "аа":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in ['ааа', 'ааб', 'абб', 'бба']])
            bot.send_message(chat_id=message.chat.id, text=f"{message.text})!", reply_markup=keyboard)
        case "аб":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in ['ааб', 'абб', 'бба', 'баа']])
            bot.send_message(chat_id=message.chat.id, text=f"{message.text})!", reply_markup=keyboard)
        case "ба":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in ['баа', 'ааа', 'ааб', 'абб']])
            bot.send_message(chat_id=message.chat.id, text=f"{message.text})!", reply_markup=keyboard)
        case "бб":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in ['бба', 'баа', 'ааа', 'ааб']])
            bot.send_message(chat_id=message.chat.id, text=f"{message.text})!", reply_markup=keyboard)
        case "ааа":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in ['аааа', 'аааб', 'аабб', 'абба']])
            bot.send_message(chat_id=message.chat.id, text=f"{message.text})!", reply_markup=keyboard)
        case "ааб":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in ['аааб', 'аабб', 'абба', 'ббаа']])
            bot.send_message(chat_id=message.chat.id, text=f"{message.text})!", reply_markup=keyboard)
        case "абб":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in ['ббаа', 'бааа', 'аааа', 'аааб']])
            bot.send_message(chat_id=message.chat.id, text=f"{message.text})!", reply_markup=keyboard)
        case "бба":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in ['абба', 'ббаа', 'бааа', 'аааа']])
            bot.send_message(chat_id=message.chat.id, text=f"{message.text})!", reply_markup=keyboard)
        case _:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in ['аа', 'аб', 'ба', 'бб']])
            bot.send_message(message.chat.id, "а!", reply_markup=keyboard)
        

bot.polling(none_stop=True)