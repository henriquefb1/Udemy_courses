#Calcular hipotenusa

from math import hypot

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
hypotenusa = hypot(n1, n2)

print(f'{hypotenusa:.2f}')