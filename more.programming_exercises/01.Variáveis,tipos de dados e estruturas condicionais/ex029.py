# Elabore um progama para verificar se um ano é bissexto ou não. A condição para ser um ano bissexto é: o ano deve ser divisível por 400; ou se for divisível por 4 e não for divisível por 100.

year = int(input('Ano: '))

if year % 400 == 0:
    print(f'O ano {year} é bissexto.')
elif year % 4 == 0 and not year % 100 == 0:
    print(f'O ano {year} é bissexto.')
else:
    print(f'O ano {year} não é bissexto.')