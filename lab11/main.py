import telebot
from telebot import types
import markups
import currency
from enum import Enum, auto

token = ''

user_states = {}

class States():
    choosing_currency = "CHOOSING_CURRENCY"
    date_start = "DATE_START"
    date_end = "DATE_END"

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def main(message):
    id = message.from_user.id
    user_states[id] = States.choosing_currency
    bot.send_message(text="Выберите валюту", chat_id=id, reply_markup=markups.currency_markup())

@bot.message_handler()
def currencie_choosen(message):
    id = message.from_user.id
    text = message.text
    currency_codes = currency.get_currencies()
    for i in currency_codes:
        
        if text == i[1]:
            user_states[id] = States.date_start+":"+text
            bot.send_message(chat_id=id, text="Введите начальную дату. Формат ввода должен быть `01/02/2025`, что соответствует 1 февраля 2025 года, либо отправьте `-`, чтобы получить последнее значение", reply_markup=None)
            return

    if user_states[id].split(':')[0] == States.date_start:
        if text == '-':
            currency_value = currency.get_currency_value(i[0])
            bot.send_message(chat_id=id, text=currency_value, reply_markup=None)
            bot.send_message(chat_id=id, text='Выберите валюту', reply_markup=markups.currency_markup)
        else:
            currency_text = user_states[id].split(':')[1]
            user_states[id] = States.date_end+":"+currency_text+":"+text
            bot.send_message(chat_id=id, text='Введите в том же формате конечную дату')
        return

    elif user_states[id].split(':')[0] == States.date_end:
        keys = user_states[id].split(':')
        currency_code = currency.get_currencies(keys[1])
        start = keys[2]
        end = text
        values = currency.get_currency_value_with_interval(currency_code, start, end)
        user_states[id] = States.choosing_currency
        if values is None:
            bot.send_message(chat_id=id, text='Неверный формат написания интервалов')
        else:
            result = " ".join(values)
            bot.send_message(chat_id=id, text=result)
        bot.send_message(chat_id=id, text='Выберите валюту', reply_markup=markups.currency_markup())
        return

bot.polling(none_stop=True)
