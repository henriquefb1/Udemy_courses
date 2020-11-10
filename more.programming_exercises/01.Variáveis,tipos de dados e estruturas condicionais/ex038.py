# Escreva um script para classificar um triângulo de acordo com o tamanho dos seus lados. Considere as seguintes informações:

# Triângulo equilátero: todos os lados possuem o mesmo tamanho;

# Trângulo escaleno: todos os lados possuem medidas diferentes;

# Triângulo isósceles: caracterizado por ter dois lados com o mesmo tamanho.

s1 = float(input('Primeiro lado: '))
s2 = float(input('Segundo lado: '))
s3 = float(input('Terceiro lado: '))

if s1 == s2 and s1 == s3:
    print('Se trata de um triângulo equilátero.')
elif s1 != s2 and s1 != s3 and s2 != s3:
    print('Se trata de um triângulo escaleno.')
elif s1 == s2 or s2 == s3 or s3 == s1:
    print('Se trata de um triângulo isósceles.')