# Utilize Compreensão em Lista (List Comprehension) para criar a lista a seguir. Observe que esses números são obtidos através da raiz quadrada de cada número no intervalo [1,50]. Utilize round() para arredondar as casas decimais.
from math import sqrt


lista = [round(sqrt(x),2) for x in range(0,51)]
print(lista)

