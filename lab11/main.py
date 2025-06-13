import os
import telebot
from telebot import types
import markups
import currency
from enum import Enum, auto
from graphs import plot_adaptive
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def plot_adaptive(data, msgID):
    filename = f"./images/{msgID}.png"
    plt.figure(figsize=(10, 6))
    plt.plot(data, linewidth=0.5)
    
    plt.title('Курс валют')
    plt.xlabel('Индекс точки')
    plt.ylabel('Значение')
    plt.grid(True, alpha=0.3)

    plt.savefig(filename)
    plt.close()

    return filename


user_states = {}

class UserState:
    step: str
    currency: str = None
    date_start: str = None

    def __init__(self, step, currency = None, date_start=None):
        self.step = step
        self.currency = currency
        self.date_start = date_start

class States(Enum):
    choosing_currency = "CHOOSING_CURRENCY"
    date_start = "DATE_START"
    date_end = "DATE_END"

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def main(message):
    id = message.from_user.id
    user_states[id] = UserState(step=States.choosing_currency)
    bot.send_message(text="Выберите валюту", chat_id=id, reply_markup=markups.currency_markup())

@bot.message_handler()
def currencie_choosen(message):
    id = message.from_user.id
    text = message.text

    currency_codes = currency.get_currencies()

    if id not in user_states:
        user_states[id] = UserState(step=States.choosing_currency)

    if user_states[id].step == States.choosing_currency:
        for i in currency_codes:
            if text == i[1]:
                user_states[id].step = States.date_start
                user_states[id].currency = i[0]
                print(user_states[id])
                bot.send_message(chat_id=id, text="Введите начальную дату. Формат ввода должен быть `01/02/2025`, что соответствует 1 февраля 2025 года, либо отправьте `-`, чтобы получить последнее значение", reply_markup=None)
                return
        bot.send_message('Неверная валюта!')
        return

    if user_states[id].step == States.date_start:
        if text == '-':
            currency_value = currency.get_currency_value(i[0])
            bot.send_message(chat_id=id, text=currency_value, reply_markup=None)
            bot.send_message(chat_id=id, text='Выберите валюту', reply_markup=markups.currency_markup())
        else:
            user_states[id].date_start = text
            user_states[id].step = States.date_end
            bot.send_message(chat_id=id, text='Введите в том же формате конечную дату')
        return

    elif user_states[id].step == States.date_end:

        start = user_states[id].date_start
        end = text
        currency_code = user_states[id].currency

        values = currency.get_currency_value_with_interval(currency_code, start, end)
        user_states[id] = States.choosing_currency
        print([type(i) for i in values])
        if values is None:
            bot.send_message(chat_id=id, text='Неверный формат написания интервалов')
        else:
            result = str(values[0]) + " " + str(values[len(values)-1])
            bot.send_message(chat_id=id, text=result)
            res = plot_adaptive(values, message.message_id)
            print(res)
            with open(res, "rb") as plot:
                bot.send_photo(chat_id=id, photo=plot)
        bot.send_message(chat_id=id, text='Выберите валюту', reply_markup=markups.currency_markup())
        return

bot.polling(none_stop=True)
