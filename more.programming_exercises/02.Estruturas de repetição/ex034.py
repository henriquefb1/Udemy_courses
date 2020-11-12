# Escreva um programa que gere 100 números aleatórios entre 1 e 1000 e armazene-os em uma lista.
from random import randint


numbers = []
for n in range(0,100):
    numbers.append(randint(0,100))
print(len(numbers))
print(numbers)