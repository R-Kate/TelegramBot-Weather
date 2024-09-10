import telebot
import requests
import json

bot = telebot.TeleBot('6613898652:AAGc8zopOiJS3RjJT3l1xcIvV-sUJlMw5No')
API = '1e1adaaf26919b79929daed41159f16f'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет. Рад тебя видеть. Напиши название города')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data['main']['temp']
        bot.reply_to(message, f"Сейчас погода: {data['main']['temp']}")

        image = 'sert.png' if temp > 5.0 else 'sert1.png'
        file = open("./" + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Город указан неверно')

bot.polling(none_stop=True)
