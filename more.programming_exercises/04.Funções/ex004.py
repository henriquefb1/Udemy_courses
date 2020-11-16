# Escreva uma função que verifique se um número é múltiplo do outro e retorne um valor lógico.

def mult_check(n1,n2):
    if n1 % n2 == 0:
        return True
    else:
        return False

a = mult_check(10,10)
b = mult_check(10,3)
print(a,b)