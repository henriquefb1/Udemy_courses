# Utilize o módulo datetime e mostre na tela a data e hora atual do sistema de acordo com o formato descrito abaixo. 12/06/2020 - 14:34:17

import datetime

date = datetime.datetime.now()

print(date.strftime('%d/%m/%Y - %H:%M:%S'))

