import math
 
num = float(input('Número: '))
log1 = math.log10(num)  
log2 = math.log(num,2)

print(f'O log de {num} na base 10 é {log1}')
print(f'O log de {num} na base 2 é {log2}')