import telebot
from telebot import types
from variables import *
from funciones import *
from config import *

bot = telebot.TeleBot(token_bot, parse_mode = None)


bot.set_my_description(description)
bot.set_my_commands(commands)
@bot.message_handler(commands=['start'])
def start(mess):
    cid = mess.chat.id
    bot.send_message(cid, saludo)
    markup = botones_inicio()
    bot.send_message(cid, "Elige una opcion", reply_markup=markup)
    
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    chat_id = message.chat.id
    mess_txt = message.text 
    if mess_txt == 'Ventas':
        bot.send_message(chat_id, products)
        markup = botones_ventas()
        bot.send_message(chat_id, op1, reply_markup=markup)
    elif mess_txt == 'salir':
        botones = botones_inicio()
        bot.send_message(chat_id, "Elige una opcion", reply_markup=botones)
    elif mess_txt == 'Ayuda <3':
        bot.send_message(chat_id, ayuda)
    elif mess_txt == 'op 1':
        botones = botones_ventas1()
        bot.send_message(chat_id, 'Ingrese una opcion', reply_markup=botones)
        bot.register_next_step_handler(message, handle_op1_input)
 

        
def handle_op1_input(message, cont=0):
    chat_id = message.chat.id
    mess_txt = message.text
    
    if mess_txt == 'Salir':
        bot.send_message(chat_id, 'Saliendo de op 1')
        start(message)
    elif mess_txt == 'Sumar':
        bot.send_message(chat_id, 'Funciono')  
        bot.register_next_step_handler(message, handle_op1_input)   
    else:
        cont += 1
        bot.send_message(chat_id, f'Seleccione una opcion valida {cont}')
        bot.register_next_step_handler(message, lambda m: handle_op1_input(m, cont))
        
bot.infinity_polling()
