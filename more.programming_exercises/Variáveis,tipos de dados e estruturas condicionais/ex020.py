# Escreva um programa que peça um número inteiro do usuário e calcule e imprima a tabuada deste número.

number = int(input('Número para geração de tabuada: '))

for counter in range(1, 11):
    print(f'{number} * {counter} = {number * counter}')
    print('-=-' * 5)

