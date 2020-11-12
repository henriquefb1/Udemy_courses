# Escreva um programa que multiplique todos os elementos de uma lista.

from random import randint


lista = []
for n in range(0,100):
    lista.append(randint(1,10))
multiplier = 1
for number in lista:
    multiplier = multiplier * number
print(lista)
print(multiplier)