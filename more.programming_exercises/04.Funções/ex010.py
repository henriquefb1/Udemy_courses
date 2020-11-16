# Escreva uma função que receba uma lista de números reais como parâmetro e retorne a média destes números.

def list_average(lista):
    return sum(lista) / len(lista)

lista = [1,2,3,4,5]

x = list_average(lista)
print(x)