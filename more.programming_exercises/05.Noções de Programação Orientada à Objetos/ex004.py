"""Crie uma classe Produto com as seguintes características:
Atributos:
Nome;
Estoque;
Descrição;
Preço.
Métodos:
Mostrar nome;
Mostrar estoque;
Mostrar preço;
Mudar nome;
Mudar estoque;
Mudar descrição;
Mudar preço;
Sumário (mostrar na tela todos os atributos de instância)."""

class Produto():
    def __init__(self, nome, estoque, descricao, preco):
        self.nome = nome
        self.estoque = estoque
        self.descricao = descricao
        self.preco = preco
    
    def get_nome(self):
        return self.nome
    def get_estoque(self):
        return self.estoque
    def get_descricao(self):
        return self.descricao
    def get_preco(self):
        return self.preco
    
    def set_nome(self, novo_nome):
       self.nome = novo_nome
    def set_estoque(self, novo_estoque):
        self.estoque = novo_estoque
    def set_descricao(self, nova_descricao):
        self.descricao = nova_descricao
    def set_preco(self, novo_preco):
        self.preco = novo_preco
    
    def summary(self):
        print(self.get_nome())
        print(self.get_estoque())
        print(self.get_descricao())
        print(self.get_preco())

produto_1 = Produto('Banana', 10, 'Fruta Amarela', 50.00)
produto_1.summary()

produto_1.set_nome('Uva')
produto_1.set_estoque(300)
produto_1.set_descricao('Fruta roxa')
produto_1.set_preco(90.00)

produto_1.summary()