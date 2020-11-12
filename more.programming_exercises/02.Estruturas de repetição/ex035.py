# Escreva um programa que gere 100 números reais aleatórios entre 0 e 1 e armazene-os em uma lista. Ao final seu programa deverá mostrar na tela as seguintes informações:
# Maior número; Menor número, Soma de todos os números gerados, Média e desvio pedrão.
from random import randint
from statistics import pstdev

lista = []

for n in range(0,100):
    lista.append(randint(0,100))

maior_valor = max(lista)
menor_valor = min(lista)
soma = 0

for number in lista:
    soma += number

average = soma / len(lista)
desvio = pstdev(lista)

print(f'O maior valor foi {maior_valor} e o menor {menor_valor}.')
print(f'A soma de todos os valores resultou em {soma}.')
print(f'A média de todos os valores resultou em {average}.')
print(f'O desvio padrão para os valores é {desvio:.2f}.')

