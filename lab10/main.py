import telebot
import requests


bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(chat_id=message.chat.id, text="ты мне сообщение, я тебе пост")


@bot.message_handler()
def post(message):
    url = f'https://api.vk.com/method/wall.post?owner_id=199724269&message={message.text}&access_token={vk_token}&v=5.199'
    r = requests.post(url)
    bot.send_message(text=f"Пост сделан: {r.status_code}", chat_id=message.chat.id)


bot.infinity_polling()