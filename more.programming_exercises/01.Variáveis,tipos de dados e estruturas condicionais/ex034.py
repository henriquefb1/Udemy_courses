# Modifique o programa anterior e permita que o usuário especifique o ano e o mês a serem mostrados na tela.

import calendar

year = int(input('Ano: '))
month = int(input('Mês: '))

print(calendar.month(year, month))

