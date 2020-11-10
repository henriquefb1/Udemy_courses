# Faça um programa que peça uma string ao usuário e mostre na tela a quantidade de caracteres.

phrase = str(input('Digite uma frase: ')).strip()
length = len(phrase)

print(f'Sua frase possui {length} caracteres.')

