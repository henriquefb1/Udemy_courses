# Converta as listas abaixo para um dicionário. Use dict() e zip().

chaves=['cidades_EUA','cidades_BR']
valores=[
    ['Nova Iorque','Houston','Boston','Detroit','Seattle'],
    ['Rio de Janeiro','São Paulo','Brasília','Goiânia','Recife']
        ]
dicty=dict(zip(chaves,valores))
print(dicty)