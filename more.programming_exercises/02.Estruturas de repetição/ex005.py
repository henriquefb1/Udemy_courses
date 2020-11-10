# Faça um programa que imprima na tela de 1 até um número digitado pelo usuário.

limit = int(input('Número: '))

if limit < 1:
    for number in range(1, (limit-1), -1):
        print(number)
elif limit > 1:
    for number in range(1, (limit+1)):
        print(number)
elif limit == 1:
    print(limit)