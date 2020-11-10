# Escreva um programa que receba dois números de ponto flutuante e mostre na tela o maior número digitado. Considere a possibilidade de o usuário digitar dois números iguais.

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))

if n1 > n2:
    print(f'O maior valor digitado foi {n1:.2f}.')
elif n2 > n1:
    print(f'O maior valor digitado foi {n2:.2f}.')
else:
    print(f'Ambos os valores digitados são iguais. {n1}.')