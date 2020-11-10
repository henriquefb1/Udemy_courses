# Escreva um script que mostre na tela o preço de um produto associado a uma categoria especificada pelo usuário.  Utilize como referência as informações a seguir. Caso o usuário não digite uma categoria válida (número entre 1 e 10) mostre na tela uma mensagem personalizada.

while True:
    category = int(input('Categoria (1-10): '))

    if category == 1:
        print(f'Preço: $ 0.50')
        break
    elif category == 2:
        print(f'Preço: $ 11.30')
        break
    elif category == 3:
        print(f'Preço : $ 17.50')
        break
    elif category == 4:
        print(f'Preço : $ 33.97')
        break
    elif category == 5:
        print(f'Preço: $ 103.47')
        break
    elif category == 6:
        print(f'Preço: $ 44.67')
        break
    elif category == 7:
        print(f'Preço: $ 12.55')
        break
    elif category == 8:
        print(f'Preço: $ 14.87')
        break
    elif category == 9:
        print(f'Preço: $ 98.12')
        break
    elif category == 10:
        print(f'Preço: $ 131.40')
        break
    else:
        print('Informação invalida, favor tentar novamente.')