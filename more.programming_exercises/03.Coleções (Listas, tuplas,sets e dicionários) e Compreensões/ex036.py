# Utilize compreensão de dicionários para construir o dicionário abaixo: {'chave1': 1, 'chave2': 4, 'chave3': 9, 'chave4': 16, 'chave5': 25, 'chave6': 36, 'chave7': 49, 'chave8': 64, 'chave9': 81}

dicty = {'chave'+str(x):x**2 for x in range(1,10)}
print(dicty)
