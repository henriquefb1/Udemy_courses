# Use a função zip() para criar uma lista de tuplas. O primeiro elemento do par deve armazenar o índice da tupla, enquanto que seu segundo elemento é o índice ao cubo. Considere um intervalo de 1 a 20.

lista = []

for x in range(1,21):
    y = x**2
    lista.append((x-1,y))

print(lista)

# Solução do site:
lista=list(zip(range(20),[numero**2 for numero in range(1,21)]))

