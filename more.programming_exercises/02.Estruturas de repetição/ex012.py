# Escreva um programa que peça números reais (float) do usuário indefinidamente . Caso os números digitados não estejam situados entre 0 e 10 o programa deverá ser finalizado, mostrando a soma e a quantidade de números digitados.

number = 0
soma = 0
numbers_typed = 0
while number >= 0 and number <= 10:
    number = float(input('Número Float: '))
    if number < 0 or number > 10:
        print(f'Soma dos números digitados: {soma}')
        print(f'Quantidade de números informados: {numbers_typed}')
        break
    soma += number
    numbers_typed += 1
