# Utilize Compreensão em Lista (List Comprehension) para criar as listas a seguir.
# [(5, 0), (6, 1), (7, 2), (8, 3), (9, 4), (10, 5), (11, 6), (12, 7), (13, 8), (14, 9)]
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81)]

list_1 = [(x,x-5) for x in range(5,15)]
print(list_1)
list_2 = [(x,x**2) for x in range(0,10)]
print(list_2)

