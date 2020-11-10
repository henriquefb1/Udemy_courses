# Escreva um programa que receba três números do usuário e mostre na tela o maior número digitado.

n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))
n3 = float(input('Número 3: '))
highest = max(n1, n2, n3)

print(f'O maior valor digitado foi {highest:.2f}.')