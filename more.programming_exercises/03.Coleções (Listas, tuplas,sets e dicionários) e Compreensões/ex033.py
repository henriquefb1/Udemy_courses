# Nos exercícios anteriores utilizamos compreensão de listas para construir listas de uma forma rápida e 'pythônica' utilizando uma notação simples. Os dicionários também suportam a mesma operação, possibilitando uma construção simples e compacta combinando loops e estruturas condicionais. Nestes termos, podemos aplicar esse conceito para criar DataFrames com pandas, uma aplicação muito comum em Data Science. Sendo assim, utilize compreensão de dicionários para construir os dicionários abaixo.

# a) a) Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, 9 (que podem ser armazenados em uma lista) e seus valores correspondem ao quadrado destes números.
new_dict = {x: x**2 for x in [1, 4, 5, 6, 7, 9]}
print(new_dict)

#b) Crie um dicionário em que suas chaves correspondem a números inteiros entre [1,10] e cada valor associado é o número ao quadrado.
new_dict_2 = {x:x**2 for x in range(1,11)}
print(new_dict_2)

#c) Crie um dicionário em que suas chaves correspondem a números de 10 a 1 e seus respectivos valores denotam o cubo de cada chave.
new_dict_3 = {x:x**3 for x in range(10,0,-1)}
print(new_dict_3)