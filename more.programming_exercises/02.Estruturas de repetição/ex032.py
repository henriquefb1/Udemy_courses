# Escreva um programa que replique o padrão de números a seguir, tal que o usuário insira o n-ésimo termo.

while True:
    number_user = int(input('Número limite: '))
    if number_user <= 0:
        print('Favor informar um valor maior que 0.')
        continue
    else:
        break
lista = []
for number in range(1,number_user+1):
    lista.append(number)
    print(lista)
