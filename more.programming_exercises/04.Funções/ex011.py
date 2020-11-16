# Escreva uma função que retorna o tamanho de uma string.

def string_len(string):
    return len(string)

x = string_len('Henrique')
print(x)

def string_len2(string):
    counter = 0
    for letter in string:
        counter += 1
    return counter

y = string_len2('Henrique')
print(y)

