# Escreva um program que solicite o nome e sobrenome do usuário e em seguida deverá apresentar o nome completo do usuário.

name = str(input('Nome: ')).strip().title()
last_name = str(input('Sobrenome: ')).strip().title()

print(f'Olá, {name} {last_name}.')