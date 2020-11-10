# Faça um programa que calcule a área de uma circunferência, recebendo apenas o valor do raio.

from math import pi

r = float(input('Raio: '))
area = pi * (r ** 2)

print(f'{area:.2f}')