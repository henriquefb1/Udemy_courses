# A partir da lista
# frutas=['  BaNanA    ', '  morangO ', ' mAçã  ','   MeLão']
# Use List Comprehension e obtenha as seguintes listas:
#['Eu gosto de Banana !', 'Eu gosto de Morango !', 'Eu gosto de Maçã !', 'Eu gosto de Melão !']
# ['BANANA', 'MORANGO', 'MAÇÃ', 'MELÃO']
# ['banana', 'morango', 'maçã', 'melão']


frutas=['  BaNanA    ', '  morangO ', ' mAçã  ','   MeLão']

like_lista = ['Eu gosto de ' + x.title().strip() + ' !' for x in frutas]
capital_lista = [x.upper().strip() for x in frutas]
lower_lista = [x.lower().strip() for x in frutas]
print(like_lista)
print(capital_lista)
print(lower_lista)