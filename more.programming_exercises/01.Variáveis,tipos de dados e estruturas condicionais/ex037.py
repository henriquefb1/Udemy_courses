# Determine se uma letra inserida pelo usuário é uma vogal ou consoante. Armazene as vogais em uma lista e implemente sua solução. Desconsidere a possibilidade de o usuário inserir números ou caracteres especiais.

letter = str(input('Letra: '))
vowels = ['a', 'e', 'i', 'o' , 'u']

if letter in vowels:
    print(f'{letter} é uma vogal.') 
else:
    print(f'{letter} não é uma vogal.')


