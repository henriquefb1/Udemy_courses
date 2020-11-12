# Escreva um programa que some todos os elementos de uma lista.

from random import randint

lista = []
for n in range(0,100):
    lista.append(randint(0,200))
soma = 0
for number in lista:
    soma += number
print(lista)
print(soma)