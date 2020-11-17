# A partir das listas abaixo,

anos=list(range(2010,2020))
chaves=['Receita produto A','Receita produto B']
valores=[
    [1001.19,1500.55,857.94,110.33,29.45,33.55,44.70,430,120,177],
    [20,33.5,91.4,4.5,111,230,900,801.2,101.4,202.6]
]

# a) um dicionário por meio das listas chaves e valores, use zip() e dict(). Resultado esperado:
# {'Receita produto A': [1001.19, 1500.55, 857.94, 110.33, 29.45, 33.55, 44.7, 430, 120, 177], 'Receita produto B': [20, 33.5, 91.4, 4.5, 111, 230, 900, 801.2, 101.4, 202.6]}

exercise_a=dict(zip(chaves,valores))
print(exercise_a)

# b) construa um DataFrame com a biblioteca pandas a partir do dicionário criado, use o construtor DataFrame() e passe a lista anos com index. Resultado esperado:

import pandas

exercise_b = pandas.DataFrame(exercise_a,index=anos)
print(exercise_b)

# c) crie uma lista de tuplas que armazene a receita total dos produtos A e B por ano. Use Compreensão em Listas. Resultado esperado: [(2010, 1021.19), (2011, 1534.05), (2012, 949.34), (2013, 114.83), (2014, 140.45), (2015, 263.55), (2016, 944.7), (2017, 1231.2), (2018, 221.4), (2019, 379.6)]

exercise_c = list(zip(anos,[round(v1+v2,2) for v1, v2 in zip(valores[0], valores[1])]))
print(exercise_c)



