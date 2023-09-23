import os
from dotenv import load_dotenv
import telebot
from telebot import types
import django
django.setup()
from malumot.models import Malumot

load_dotenv()
BOT_TOKEN = os.getenv('BOT')

bot = telebot.TeleBot(BOT_TOKEN)
sarlavhalar = []
malumotlar = []

def data_cell():
    db = Malumot.objects.all()
    malumott: Malumot
    for malumott in db:
        sarlavhalar.append(malumott.sarlovha)
        malumotlar.append(malumott.malumot)
data_cell()


def start_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    Catalog = types.KeyboardButton(text=sarlavhalar[0])
    Info = types.KeyboardButton(text=sarlavhalar[1])
    keyboard.add(Catalog, Info)
    return keyboard




    
@bot.message_handler(commands=['start'])
def start_message(message: types.Message):
  bot.send_message(message.from_user.id,"Bulardan birini tanlang.", 
                   reply_markup=start_keyboard())



bot.infinity_polling()