# Considere um número inteiro positivo n especificado pelo usuário. Elabore um programa que calcule e mostre na tela:
# A soma dos n primeiros números inteiros não-nulos (1+2+3+ ... +n) ;
# A soma dos n primeiros números pares;
# A soma dos n primeiros números ímpares.


number = 0
soma_total = 0
soma_par = 0
soma_impar = 0

while number == 0:
    number = int(input('Número (0 Não aceitável): '))

for n in range(0,number+1):
    soma_total += n
    if n % 2 == 0:
        soma_par += n
    else:
        soma_impar += n

print(f'A soma de todos os valores é: {soma_total}.')
print(f'A soma de todos os valores pares é: {soma_par}.')
print(f'A soma de todos os valors ímpares é: {soma_impar}.')

