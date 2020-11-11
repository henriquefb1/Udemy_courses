# Elabore um programa que calcule e mostre na tela os números pares entre 1 e 200.

for n in range(1,201):
    if n % 2 == 0:
        print(n, end=' ')