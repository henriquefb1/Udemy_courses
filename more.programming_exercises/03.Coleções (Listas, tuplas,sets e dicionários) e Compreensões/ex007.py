# Ordene os elementos das listas a seguir em ordem crescente e decrescente.


lista1=[117, 1519, 1335, 1600, 1676, 1491, 868, 
        1149, 642, 1321, 509, 1296, 1936, 1014, 
        1114, 1197, 94, 1347, 1112, 1224, 351, 
        1498, 1028, 255, 937, 514, 1041, 1923, 
        913, 510, 868, 1195, 1218, 1489, 1920, 
        630, 666, 605, 515, 1219, 59, 1217, 1293, 
        487, 1095, 1730, 1115, 1465, 1506, 1881]

print(f'Lista1 em ordem crescente:\n{sorted(lista1)}')
print('\n')
print(f'Lista1 em ordem decrescente:\n{sorted(lista1, reverse=True)}')

lista2=['a','a','z','f',
        'h','i','m','u',
        'q','r','b','d',
       ]

print('\n')
print(f'Lista2 em ordem crescente:\n{sorted(lista2)}')
print('\n')
print(f'Lista2 em ordem decrescente:\n{sorted(lista2, reverse=True)}')
