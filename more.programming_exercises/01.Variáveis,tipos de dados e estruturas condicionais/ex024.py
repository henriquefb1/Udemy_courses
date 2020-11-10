# O Índice de Massa Corporal (IMC) é utilizado para mensurar o peso ideal de uma pessoa. Escreva um programa que peça o nome, a idade , o peso e a altura do usuário. Ao final calcule e mostre o resultado do seu IMC e classifique este resultado de acordo com a regra a seguir. Lembre que: IMC=massa/(altura*altura)

weight = float(input('Peso(KG): '))
height = float(input('Altura(M): '))
imc = weight / (height * height)

if imc < 17:
    print(f'{imc:.2f}, muito abaixo do peso ideal.')
elif imc <= 18.5:
    print(f'{imc:.2f}, abaixo do peso.')
elif imc <= 25:
    print(f'{imc:.2f}, peso normal.')
elif imc <= 30:
    print(f'{imc:.2f}, acima do peso.')
elif imc <= 35:
    print(f'{imc:.2f}, obesidade I.')
elif imc <= 40:
    print(f'{imc:.2f}, obesidade II (severa).')
else:
    print(f'{imc:.2f}, obesidade III (mórbida).')