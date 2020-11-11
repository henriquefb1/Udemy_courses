# Elabore um programa para imprimir a sequência de Fibonacci até o n-ésimo termo definido pelo usuário. Certifique que o usuário digite um número inteiro positivo.

while True:
    end = int(input('Final para sequência de Fibonacci: '))
    if end <= 0:
        print(f'Favor informar um valor positivo. Negativos e Nulos não contam.')
        continue
    else:
        break

n1 = 0
n2 = 1

while n1 <= end or n2 <= end:
    print(f'{n1}, {n2},', end=' ')
    n1 = n1 + n2
    n2 = n2 + n1
