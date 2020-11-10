# Utilizando estruturas de repetição escreva um programa que mostre os resultados da tabuada (multiplicação) de um número inserido pelo usuário.


number = int(input('Número: '))
multiplier = 1

while multiplier < 11:
    print(f'{number} * {multiplier} = {number * multiplier}')
    multiplier += 1