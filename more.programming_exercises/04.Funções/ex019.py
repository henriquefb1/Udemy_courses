# Considere a lista nomes a seguir e responda: nomes=['','Roberto Carlos','Tom Jobim','Jorge Amado','Machado de Assis','Zé Ramalho','Elba Ramalho','','',[],()]

nomes=['','Roberto Carlos','Tom Jobim','Jorge Amado','Machado de Assis','Zé Ramalho','Elba Ramalho','','',[],()]

lista = list(filter(lambda x:len(x)>0, nomes))
print(lista)

lista_2 = list(filter(lambda x:'Ramalho' in x, nomes))
print(lista_2)