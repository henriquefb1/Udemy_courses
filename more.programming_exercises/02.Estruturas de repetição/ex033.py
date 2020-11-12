# Ordene em ordem crescente/decrescente das músicas mais tocadas.

lista=[
	('Música3',{'toques':137}),
	('Música7',{'toques':2}),
	('Música11',{'toques':30}),
	('Música9',{'toques':45}),
	('Música10',{'toques':79}),
	('Música2',{'toques':190}),
	('Música8',{'toques':201}),
	('Música5',{'toques':44}),
	('Música1',{'toques':29}),
	('Música6',{'toques':14}),
	('Música4',{'toques':14}),
]

menos_tocadas = sorted(lista, key=lambda x:x[1]['toques'])
mais_tocadas = sorted(lista, key=lambda x:x[1]['toques'], reverse=True)

print(menos_tocadas)
print(mais_tocadas)
