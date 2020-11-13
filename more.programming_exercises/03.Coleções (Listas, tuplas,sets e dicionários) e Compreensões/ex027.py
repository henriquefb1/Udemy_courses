# A partir das listas

linguagens=['php','JavaScript']
frases=['Eu amo ','Eu odeio ']

#Use List Comprehension e obtenha a seguinte lista:
#['Eu amo php !', 'Eu odeio php !', 'Eu amo JavaScript !', 'Eu odeio JavaScript !']

nova_lista = [x+y+' !' for x in frases for y in linguagens]
print(nova_lista)

nova_lista2 = []
for x in frases:
    for y in linguagens:
        nova_lista2.append(x+y+' !')
print(nova_lista2)
