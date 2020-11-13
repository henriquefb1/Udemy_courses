# Utilize Compreensão em Lista (List Comprehension) para criar a lista a seguir. Ademais, tente resolver este problema sem usar Compreensão em Lista.

lista1=[]
for x in [1,2,3]:
     for y in [3,1,4]:
        if x != y:
            lista1.append((x, y))

lista2=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

