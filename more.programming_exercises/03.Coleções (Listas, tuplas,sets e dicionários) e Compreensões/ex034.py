# A partir da lista: linguagens = ['python', 'javascript', 'java', 'php', 'c', 'julia']
# Use Dict Comprehension para construir o dicionário abaixo: {'python': 6, 'javascript': 10, 'java': 4, 'php': 3, 'c': 1, 'julia': 5}


linguagens = ['python', 'javascript', 'java', 'php', 'c', 'julia']

new_dict = {x:len(x) for x in linguagens}
print(new_dict)

