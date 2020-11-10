# Faça um programa que recebe um número e apresenta sua raiz quadrada.

from math import sqrt

n = float(input('Número: '))
square_root = sqrt(n)

print(f'A raiz quadrade de {n:.2f} é {square_root:.2f}.')
