"""Crie uma classe Pessoa com as seguintes características:
Atributos:
Nome (atributo público);
E-mail (atributo público);
Senha (atributo privado).
Métodos:
Mostrar nome;
Mostrar E-mail;
Mostrar senha.
Crie um objeto da classe Pessoa para testar suas propriedades e métodos."""

class Pessoa():
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.__senha = senha
    
    def get_name(self):
        return self.nome
    def get_email(self):
        return self.email
    def get_senha(self):
        return self.__senha

user = Pessoa('Henrique', 'henriquebarreiros2@hotmail.com', 'henrique1%')
print(f'Nome: {user.get_name()}')
print(f'E-mail: {user.get_email()}')
print(f'Senha: {user.get_senha()}')
