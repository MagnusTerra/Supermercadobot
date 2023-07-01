import telebot
from telebot import types
from variables import *
from funciones import *
token_bot = '5849787049:AAEyzVG43-QlJPWPIJ2wMbsDGE4gXqOz4Vg'

bot = telebot.TeleBot(token_bot, parse_mode = None)

@bot.message_handler(commands=['start'])
def start(mess):
    cid = mess.chat.id
    bot.send_message(cid, saludo)
    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('Compras')
    itembtnv = types.KeyboardButton('Ventas')
    itembtnc = types.KeyboardButton('Consultas')
    itembtnd = types.KeyboardButton('Ayuda <3')
    markup.row(itembtna, itembtnv)
    markup.row(itembtnc, itembtnd)
    bot.send_message(cid, "Elige una opcion", reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def texto(mess):
    list_prod = []
    total = 0
    chat_id = mess.chat.id
    mess_txt = mess.text 
    if mess_txt == 'Ventas':
        bot.send_message(chat_id, products)
        markup = types.ReplyKeyboardMarkup()
        itembtna = types.KeyboardButton('op 1')
        itembtnv = types.KeyboardButton('op 2')
        itembtnc = types.KeyboardButton('op 3')
        itembtnd = types.KeyboardButton('op 4')
        itembtnz = types.KeyboardButton('salir')
        markup.row(itembtna, itembtnv, itembtnc, itembtnd, itembtnz)
        bot.send_message(chat_id, op1, reply_markup=markup)
    elif mess_txt == 'salir':
        botones = botones_inicio()
        bot.send_message(chat_id, "Elige una opcion", reply_markup=botones)
    elif mess_txt == 'Ayuda <3':
        bot.send_message(chat_id, ayuda)
    elif mess_txt == 'op1':
        list_prod.append('1.Cocacola 2L = L.46')
        total += 46
        vara = f'{list_prod} que es igual a {total}'
        bot.send_message(chat_id, vara)
bot.infinity_polling()