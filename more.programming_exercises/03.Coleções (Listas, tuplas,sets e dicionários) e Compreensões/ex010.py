# Considere a lista a seguir e escreva um programa para remover os elementos duplicados.

lista=[
    'a','a','a',
    'b','c','k',
    'a',1,2,3,4,
    'j','l','m',
]

new_list = []

for value in lista:
    if value not in new_list:
        new_list.append(value)
    else:
        continue

lista = new_list
print(lista)
print(list(set(lista)))