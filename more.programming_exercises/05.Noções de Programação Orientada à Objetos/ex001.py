# Crie uma classe Pessoa com os seguintes atributos: nome, sobrenome e idade.

class Pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    

p1 = Pessoa('Henrique', 'Barreiros', 28)
print(f'{p1.nome} {p1.sobrenome}, idade:{p1.idade} anos.')
