# Escreva um programa que peça ao usuário números entre 0-10. Se o usuário inserir um número fora desse intervalo o programa deverá finalizar com uma mensagem personalizada.

n = 0
while n >= 0 and n <= 10:
    n = int(input('Número: '))
    if n < 0 or n > 10:
        print('Fim de programa')
        break