# Implemente uma calculadora simples com as operações aritméticas básicas. O usuário deverá especificar a operação desejada (+,-,*,/) e seguidamente inserir dois valores. Caso, o usuário escolha divisão e insira o valor do denominar 0 mostre uma mensagem personalizada. Para os demais casos, mostre na tela o resultado da operação desejada.

choice_list = ['+', '-', '*', '/']
while True:
    choice = str(input('Opção de operação ( +, -, *, /): '))
    if choice not in choice_list:
        print('Informação inválida, favor escolher entre (+, -, *, /).')
        continue
    if choice == '+':
        print('Você optou por soma (+).')
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
        result = n1 + n2
        print(f'{n1} + {n2} = {result}')
        continuation = int(input('Gostaria de continuar ou finalizar? [1] para continuar e [0] para finalizar: '))
        if continuation == 1:
            continue
        elif continuation == 0:
            break
    elif choice == '-':
        print('Você optou por subtração (-).')
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
        result = n1 - n2
        print(f'{n1} - {n2} = {result}')
        continuation = int(input('Gostaria de continuar ou finalizar? [1] para continuar e [0] para finalizar: '))
        if continuation == 1:
            continue
        elif continuation == 0:
            break
    elif choice == '*':
        print('Você optou por multiplicação (*).')
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
        result = n1 * n2
        print(f'{n1} * {n2} = {result}')
        continuation = int(input('Gostaria de continuar ou finalizar? [1] para continuar e [0] para finalizar: '))
        if continuation == 1:
            continue
        elif continuation == 0:
            break
    elif choice == '/':
        print('Você optou por divisão (/).')
        n1 = float(input('Primeiro número: '))
        while True:
            n2 = float(input('Segundo núnero: '))
            if n2 == 0:
                print('Favor escolher outro número para a divisão, dividir por 0 não é possível.')
                continue
            else:
                break
        result = n1 / n2
        print(f'{n1} / {n2} = {result}')
        continuation = int(input('Gostaria de continuar ou finalizar? [1] para continuar e [0] para finalizar: '))
        if continuation == 1:
            continue
        elif continuation == 0:
            break
        




