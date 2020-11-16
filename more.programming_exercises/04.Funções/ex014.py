# Escreva uma função que verifique se duas listas possuem ao menos um elemento em comum, retornando True em caso positivo.

def lista_comp(list1, list2):
    for value in list1:
        for value_2 in list2:
            if value == value_2:
                return True
    else:
        return False
    
print(lista_comp([1,2,3,4,5],[5,10,15,20]))
            