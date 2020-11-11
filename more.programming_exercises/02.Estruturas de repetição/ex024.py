# Escreva um programa para checar se um determinado número é primo ou não.
# Lembrete: um número primo pode ser dividido por apenas dois números, quais sejam: ele mesmo e o número um.

while True:
    number = int(input('Número: '))
    if number == 0 or number == 1 or number == 2:
        print(f'Não informar um valor nulo ou 1, 2.')
        continue
    for n in range(2, number):
        if number % n == 0:
            print('O número não é primo.')
            break
        else:
            print(f'O número é primo.')
            break
    choice = int(input('Deseja tentar novamente[1] ou sair[0]? '))
    if choice == 1:
        continue
    else:
        break
    