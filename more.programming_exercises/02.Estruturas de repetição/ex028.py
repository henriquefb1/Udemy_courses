# Escreva um programa para somar todos os números naturais em um intervalo definido pelo usuário.

while True:
    number = int(input('Número: '))
    if number <= 0:
        print(f'O valor informado não pode ser negativou ou nulo, tentar novamente.')
    else:
        break
soma = 0
for value in range(0, number + 1):
    soma += value
print(f'A soma de todos os números até o número informado é: {soma}.')

    
