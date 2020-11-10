# Escreva um programa que solicite o nome, o sobrenome e o salário atual de um funcionário. Ao fim, calcule seu novo salário considerando cenários hipotéticos, com os seguintes aumentos: 10%, 25%,30% e 50%. A mensagem na tela deverá seguir o seguinte padrão:

name = str(input('Nome: ')).strip().title()
last_name = str(input('Sobrenome: ')).strip().title()
salary = float(input('Salário atual: R$'))
salary_10 = salary * 1.10
salary_25 = salary * 1.25
salary_30 = salary * 1.30
salary_50 = salary * 1.50

print(f'Olá {name} {last_name}.')
print('-=-' * 20)
print(f'Seu salário atual é R${salary:.2f}.')
print('-=-' * 20)
print(f'Seu salário com 10% de aumento é: {salary_10:.2f}.')
print('-=-' * 20)
print(f'Seu salário com 25% de aumento é: {salary_25:.2f}.')
print('-=-' * 20)
print(f'Seu salário com 30% de aumento é: {salary_30:.2f}.')
print('-=-' * 20)
print(f'Seu salário com 50% de aumento é: {salary_50:.2f}.')


