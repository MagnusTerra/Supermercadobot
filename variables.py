import telebot

saludo = 'Soy un bot de administracion de supermercado'

products = '1.Cocacola 2L = L.46 \n2.Pan molde L.30\n3.Salchipapas = L.65\n4.Pringles Grandes = L.100'

op1 = 'Selecciona una opcion'

ayuda = 'Nos quiere donar a este enlace doname.com/SystemAkari' 


description = f'Este es un bot de adminitracion de un SuperMercado'


commands = [
    telebot.types.BotCommand('start', 'Comando de inicio del Bot'),
    telebot.types.BotCommand('help', 'Recibe la lista de comandos del Bot'),
]

name_es = 'SuperMercado Terceros'

