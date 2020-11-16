# Escreva uma função que faça uma cópia de uma lista.

def copy_list(lista):
    x = []
    for value in lista:
        x.append(value)
    return x


lista = [1,2,3,4,5]

x = copy_list(lista) 
print(x)