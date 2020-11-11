#Elabore um programa que embaralhe a lista a seguir e mostre na tela cada elemento.
#lista=['A','B','C','D','E','F','G','H','I','J','K','L','M'] 
from random import shuffle

lista = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
shuffle(lista)

print(lista)