# Escreva um programa que verifique se um determinado número digitado pelo usuário é nulo, positivo ou negativo.

n = float(input('Número: '))

if n > 0:
    print(f'O valor {n} é positivo.')
elif n < 0:
    print(f'O valor {n} é negativo.')
else:
    print(f'Você digitu 0, sendo esse um valor nulo.')