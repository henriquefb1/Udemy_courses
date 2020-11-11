# Peça 5 números do usuário e mostre na tela a média dos números digitados.

soma = 0
for number in range(1,6):
    soma =+ int(input('Número: '))

print(f'Total:{soma} \nMédia:{soma/5:.2f}')