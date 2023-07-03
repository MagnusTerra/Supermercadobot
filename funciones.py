from telebot import types
from variables import *

def botones_inicio():
    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('Comprar')
    itembtnv = types.KeyboardButton('Ventas')
    itembtnc = types.KeyboardButton('Consultas')
    itembtnd = types.KeyboardButton('Ayuda <3')
    markup.row(itembtna, itembtnv)
    markup.row(itembtnc, itembtnd)
    return markup

def botones_ventas():
    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('op 1')
    itembtnv = types.KeyboardButton('op 2')
    itembtnc = types.KeyboardButton('op 3')
    itembtnd = types.KeyboardButton('op 4')
    itembtnz = types.KeyboardButton('salir')
    markup.row(itembtna, itembtnv, itembtnc, itembtnd, itembtnz)
    return markup

def botones_ventas1():
    markup = types.ReplyKeyboardMarkup(True)
    markup.row('Salir', 'Sumar', 'AAA')
    return markup