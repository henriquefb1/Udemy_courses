# Escreva um programa que permita o acesso apenas se o usuário tiver 18 anos ou mais.

nome = str(input('Nome: ')).strip().title()
age = int(input('Idade: '))

if age >= 18:
    print(f'Bem-vindo ao nosso site {nome}.')
else:
    print(f'Você não pode acessar nosso site {nome}, apenas para maiores de 18 anos.')