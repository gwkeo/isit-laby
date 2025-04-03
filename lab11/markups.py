from telebot import types
import currency

def currency_markup():
    currencies = ['AZN', 'USD', 'EUR', 'CNY']
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*currencies)
    return markup