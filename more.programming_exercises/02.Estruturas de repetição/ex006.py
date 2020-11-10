# Escreva um programa que mostre na tela os 20 primeiros múltiplos de 5.

lista = []
x = 1

while len(lista) < 20:
    if x % 5 == 0:
        lista.append(x)
        x += 1
    x += 1

print(lista)