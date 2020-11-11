# Elabore um programa que calcule e mostre na tela os números ímpares entre 1 e 200. 

for n in range(1,201):
    if n % 2 == 1:
        print(n, end=' ')