# Crie uma função que recebe um número e verifique se este é par. Posteriormente, use a função filter() para criar uma lista com todos os números pares de 1 a 50.

def even(number):
    return number % 2 == 0

print(even(2))

lista = list(filter(lambda x:x % 2 == 0, range(1,51)))
print(lista)