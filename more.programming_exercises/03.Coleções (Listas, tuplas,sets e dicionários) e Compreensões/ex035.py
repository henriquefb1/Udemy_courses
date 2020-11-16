# A partir da lista: frutas = ['  Banana  ', ' Laranja   ', '  Maçã', ' Melão ']
# Use Dict Comprehension para construir o dicionário abaixo: {'1': 'Banana', '2': 'Laranja', '3': 'Maçã', '4': 'Melão'}

frutas = ['  Banana  ', ' Laranja   ', '  Maçã', ' Melão ']

dicty = {str(y+1):x.strip() for y, x in enumerate(frutas)}
print(dicty)
