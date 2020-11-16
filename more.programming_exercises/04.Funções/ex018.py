# a) Utilize a função map() para criar uma lista com o quadrado de cada número par e o cubo de cada número ímpar. Considere o intervalo [1,20].

lista = list(map(lambda x:(x,x**2) if x % 2 == 0 else (x,x**3),range(1,21)))
print(lista)

# b) Utilize a função map() para criar uma lista com o os números divisíveis por 3 e 5, no intervalo [1,10]. Se o número não for divisível calcule sua raiz quadrada.

lista_2 = list(map(lambda x:x if x % 3 == 0 and x % 5 == 0 else round(x ** 0.5, 2),range(1,10)))
print(lista_2)