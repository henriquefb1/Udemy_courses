# Acrescente a classe Pessoa um método para mostrar os dados de uma pessoa. Crie um objeto do tipo Pessoa para testar suas propriedades e métodos.

class Pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    
    def get_information(self):
        print(self.nome, self.sobrenome, self.idade)

p1 = Pessoa('Henrique', 'Barreiros', 28)
p1.get_information()