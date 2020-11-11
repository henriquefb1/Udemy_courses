# Escreva um programa que peça números inteiros positivos indefinidamente e armazene-os em uma lista. O programa deverá ser encerrado caso o número digitado seja negativo ou nulo. Ao final mostre na tela a quantidade números pares e ímpares.

numbers = []
even = []
odd = []
number = 1

while True:
    number = int(input('Número: '))
    if number == 0:
        break
    numbers.append(number)
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print(f'Números:{numbers} \nPares:{even} \nÍmpares:{odd}')
