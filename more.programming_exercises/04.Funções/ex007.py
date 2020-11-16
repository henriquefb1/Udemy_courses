# Elabore uma função que receba um número inteiro e retorne o fatorial deste número.

def fatorial(number):
    for x in range(number,1,-1):
        number += number * (x-1)
    return number

x = fatorial(10)
print(x)