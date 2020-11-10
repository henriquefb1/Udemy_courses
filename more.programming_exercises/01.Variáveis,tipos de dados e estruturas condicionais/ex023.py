# Escreva um programa que peça um número inteiro do usuário e mostre se esse número é par ou ímpar. A mensagem na tela deverá seguir o seguinte formato:

number = int(input('Número inteiro: '))

if number % 2 == 0:
    print(f'O número {number} é PAR.')
else:
    print(f'O número {number} é IMPAR.')