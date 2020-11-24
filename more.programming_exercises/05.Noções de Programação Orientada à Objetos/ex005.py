"""Crie uma classe Lampada com os seguintes atributos e métodos:
Atributos:
Cor;
Voltagem;
Luminosidade;
Ligada (a lâmpada deve inicializar desligada).
Métodos:
Verificar se a lâmpada está ligada/desligada
Ligar/desligar a lâmpada.
Todos os atributos devem ser privados.
Crie um objeto da classe Lampada e teste os métodos criados."""

class Lamp():
    def __init__(self, cor, voltagem, luminosidade, ligada=False):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.ligada = False
    
    def turn_on(self, ligada=True):
        print(f'{self} está ligado.')
    def turn_off(self, ligada=False):
        print(f'{self} está desligado.')
    def on_off_check(self):
        if self.ligada==False:
            print('Desligado.')
        else:
            print('Ligado')

lamp_1 = Lamp('Amarelo', '120V', 'Muito clara')
lamp_1.turn_on()
lamp_1.turn_off()
lamp_1.on_off_check()
