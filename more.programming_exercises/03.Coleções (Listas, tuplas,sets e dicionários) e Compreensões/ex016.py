# Considere a tupla1 e responda as seguintes questões: a) mostre na tela o tamanho desta tupla;b) ordene a tupla e mostre o resultado na tela;c) mostre na tela o número de ocorrências da string 'A';d) mostre na tela o número de ocorrências da string 'B';e) mostre na tela o índice da string 'X';f) mostre na tela o último elemento da tupla1.

tupla1=('A','B','A','Z','Z','X','A','E','K','G','H')

print(len(tupla1)) #a) mostre na tela o tamanho desta tupla
print(sorted(tupla1)) #b) ordene a tupla e mostre o resultado na tela
A_counter = 0
B_counter = 0
for value in tupla1:
    if value == 'A':
        A_counter += 1
    elif value == 'B':
        B_counter += 1
print(A_counter) #c) mostre na tela o número de ocorrências da string 'A
print(B_counter) #d) mostre na tela o número de ocorrências da string 'B'
print(tupla1.index('X')) #e) mostre na tela o índice da string 'X'
print(tupla1[-1]) #f) mostre na tela o último elemento da tupla1