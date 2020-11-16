# Escreva uma função para checar se uma lista é vazia ou não.

def list_checker(lista):
    if len(lista) == 0:
        return 'Lista vazia'
    else:
        return 'Lista não vazia'

listy = [1]

x = list_checker(listy)
print(x)