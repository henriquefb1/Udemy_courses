# Use compreensão de dicionários e obtenha os dicionários a seguir:

from math import log2

# a) {2: 1.0, 4: 2.0, 6: 2.585, 8: 3.0, 10: 3.322, 12: 3.585, 14: 3.807, 16: 4.0, 18: 4.17, 20: 4.322}

dicty = {x:round(log2(x),2) for x in range(2,21,2)}
print(dicty)


# b) {'C': 3, 'E': 5, 'F': 6, 'I': 9, 'J': 10, 'L': 12, 'O': 15, 'R': 18, 'T': 20}

dicty_2 = {chr(64+number):number for number in range(1,21) if number % 5 == 0 or number % 3 == 0}
print(dicty_2)

