import sqlite3
import telebot

bot = telebot.TeleBot("6426042253:AAFhQRS9VwI84DW65oNyDHIb8n6wgQ_b20A")

user_age = None
user_height = None

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

@bot.message_handler(commands=['start'])
def start_message(message):
    global user_age
    global user_height
    user_age = None
    user_height = None
    bot.send_message(message.chat.id, "Привет! Какой у тебя возраст?")

@bot.message_handler(func=lambda message: True)
def ask_age(message):
    global user_age
    if is_number(message.text):
        user_age = float(message.text)
        bot.send_message(message.chat.id, "Какой у тебя рост?")
        bot.register_next_step_handler(message, save_height)
    else:
        bot.send_message(message.chat.id, "Неправильные данные. Введите число.")

def save_height(message):
    global user_height
    if is_number(message.text):
        user_height = float(message.text)
        bot.send_message(message.chat.id, "Спасибо! Данные сохранены.")
    else:
        bot.send_message(message.chat.id, "Неправильные данные. Введите число.")

bot.polling(none_stop=True)
