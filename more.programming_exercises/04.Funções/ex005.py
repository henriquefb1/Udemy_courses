# Escreva um programa que pesquise um determinado valor em uma lista. Sua função deve ter como parâmetros a lista e o valor a ser verificado. Caso o valor faça parte da lista informada retorne True e False, caso contrário.

def list_checker(list, value):
    return value in list

lista = [1,2,3,4,5]

x = list_checker(lista, 5)
y = list_checker(lista, 10)

print(x, y)