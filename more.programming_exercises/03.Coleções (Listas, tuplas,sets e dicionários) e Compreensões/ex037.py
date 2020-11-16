# Utilize compreensão de dicionários para construir o dicionário abaixo: {'A': 1, 'B': 2, 'C': 6, 'D': 24, 'E': 120}
from math import factorial


dicionario = {chr(64+i):factorial(i)  for i in range(1,6)}
print(dicionario)