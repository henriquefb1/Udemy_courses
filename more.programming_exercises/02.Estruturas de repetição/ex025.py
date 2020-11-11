# Elabore um programa para imprimir todos os números primos existentes em um intervalo delimitado pelo usuário.

while True:
    start = int(input('Número de começo: '))
    if start == 1 or start == 2 or start == 0:
        print(f'Número 0, 1, 2 não são aceitos.')
        continue
    else:
        break
while True:
    end = int(input('Número de final: '))
    if end <= start:
        print(f'O valor final precisa ser maior do que o começo, favor inserir novamente.')
        continue
    else:
        break

for number in range(start, end+1):
    for number_2 in range(2, number):
        if number % number_2 == 0:
            break
    else:
        print(number)
            
