# Escreva um programa que receba nome, sobrenome e idade de um usuário e apresente as informações.

nome = str(input('Nome: ')).strip().title()
sobrenome = str(input('Sobrenome: ')).strip().title()
idade = int(input('Idade: '))

print(f'Olá, {nome} {sobrenome}, você possui {idade} anos de idade.')