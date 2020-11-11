# Escreva um programa que peça ao usuário 20 números reais e ao final mostre a soma e a média dos números digitados.

number = 0
summ = 0
average = 0
counter = 0

for n in range(0,21):
    number = int(input('Número: '))
    summ += number
    counter += 1
print(f'Soma: {summ} \nMédia: {summ / counter}')
