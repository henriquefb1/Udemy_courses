# Escreva um programa que peça 5 números inteiros não-nulos ao usuário e mostre na tela o quadrado de cada número digitado.
numbers = []
cube = []
counter = 0 

while counter != 5:
    number = int(input('Número: '))
    if number == 0:
        print('Número não contabilizado, o valor não pode ser nulo.')
        continue
    else:
        numbers.append(number)
        cube.append(number**2)
        counter += 1
for n in range(0,5):
    print(f'{numbers[n]} - {cube[n]}.')
    

