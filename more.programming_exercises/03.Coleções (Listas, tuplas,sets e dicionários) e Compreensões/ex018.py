#18.1 Crie um script para iterar no dicionário abaixo e mostrar na tela todas as suas chaves, uma a uma.

produto1={
    'nome':'produto1',
    'tipo':'categoriaA',
    'valor':'50.5',
    'fornecedor':'ABCD',
}
for item in produto1:
    print(item)

#18.2 Crie um script para iterar no dicionário produto1 e mostrar na tela todos os seus valores, um a um.

for value in produto1.values():
    print(value)

#18.3 Crie um script para iterar no dicionário produto1 e mostrar chave,valor na tela.

for value in produto1.items():
    print(value)

