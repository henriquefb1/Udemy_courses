# Escreva um programa que replique o padrão de caracteres descrito a seguir.

for counter in range(1,12):
    print('*'*counter)
    if counter == 11:
        for counter in range(12,0,-1):
            print('*'*counter)