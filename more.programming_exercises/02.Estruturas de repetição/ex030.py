# Considere a lista abaixo e escreva um programa que mostre na tela a quantidade de números pares e ímpares.


lista=[944, 52, 161, 436, 77, 217, 
616, 639, 280, 277, 907, 735, 321, 
194, 736, 130, 793, 148, 799, 631, 
906, 417, 186, 913, 446, 537, 86, 75, 
328, 77, 899, 481, 303, 997, 212, 217,
696, 391, 402, 800, 709, 293, 9, 700, 
108, 253, 562, 166, 252, 315, 655, 680,
944, 8, 850, 765, 821, 216, 685, 666,
860, 32, 492, 880, 714, 424, 270, 308,
641, 83, 555, 807, 840, 724, 193, 256, 
556, 665, 902, 714, 564, 13, 903, 625, 14, 
551, 301, 915, 633, 781, 427, 517, 372, 
164, 469, 194, 5, 818, 776,
] 
even_count = 0
odd_count = 0
for number in lista:
    if number % 2 == 0:
        even_count += 1
    elif number % 2 == 1:
        odd_count += 1
print(f'Quantidade de valores pares:{even_count}.')
print(f'Quantidade de valores ímpares:{odd_count}.')