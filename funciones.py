import telebot
from telebot import types
from variables import *

def botones_inicio():
    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('Compras')
    itembtnv = types.KeyboardButton('Ventas')
    itembtnc = types.KeyboardButton('Consultas')
    itembtnd = types.KeyboardButton('Ayuda <3')
    markup.row(itembtna, itembtnv)
    markup.row(itembtnc, itembtnd)
    return markup