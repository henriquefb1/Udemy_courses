# Use list() e zip() para criar uma nova lista de tuplas com as listas a seguir.

paises=['Brasil','Brasil','Brasil','EUA','EUA','EUA','EUA']
estados=['São Paulo','Bahia','Rio de Janeiro','Alabama','Alabama','Alabama','Califórnia']
cidades=['São Paulo','Salvador','Rio de Janeiro','Birmingham','Huntsville','Mobile','Beverly Hills']
lista=list(zip(paises,estados,cidades))
print(lista)
