# vamos ver heranças

class Veiculo():
    def __init__(self,nome, pot, peso, rmax):
        self._rmax = rmax  #Usar dois underlines faz do atributo privado, indica que ele não deve ser usado diretamente mas sim deve ser invocado através de uma def categorizada com o decorador @proprty que retorna o atributo secreto, a def pode ter o nome do atributo sem os underscores.
        self.potencia = pot #Porém usa-se apenas um underline quando queremos indicar que um atributo é privado mas é herdado por outras classes (objetos), ou seja se uma classe for usadam como mãe, seus atributos privados devem ser acessados na criação de outros objetos, por isso um underline. Caso os dois underlines fossem mantiddos, classes filhas teriam que se referir a tal atributo como _[class name]__[atribute]
        self.peso = peso
        self.nome = nome.lower().title()
        self.pesopot = peso/pot #atributo interno da classe mãe, vaoms ver como ele é passado 

    @property
    def rmax(self):
        return self._rmax

    def __str__(self, ):
        return f'Veículo: {self.nome}\n Potência: {self.potencia}\n Peso: {self.peso}\n Peso/Pot: {self.pesopot}'

class Carro(Veiculo):
    def __init__(self, nome, pot, peso, rmax, aut):
        super().__init__(nome, pot, peso, rmax)
        self.autonomia = aut

    def __str__(self, ):
        return f'Veículo: {self.nome}\n Potência: {self.potencia} hp\n Peso: {self.peso} Kg\n Peso/Pot: {self.pesopot} Kg/hp\n Autonomia: {self.autonomia} Km\n'
    

class Moto(Veiculo):
    def __init__(self, nome, pot, peso, rmax, vmax):
        super().__init__(nome, pot, peso, rmax)
        self.vmax=vmax

    def __str__(self, ):
        return f'Veículo: {self.nome}\n Potência: {self.potencia} hp\n Peso: {self.peso} Kg\n Peso/Pot: {self.pesopot} Kg/hp\n Velocidade Máxima: {self.vmax} Km/h\n'

class Caminhão(Veiculo):
    def __init__(self, nome, pot, peso, rmax, cargamax):
        super().__init__(nome, pot, peso, rmax)
        self.cargamax = cargamax

    def __str__(self, ):
        return f'Veículo: {self.nome}\n Potência: {self.potencia} hp\n Peso: {self.peso} Kg\n Peso/Pot: {self.pesopot} Kg/hp\n Rotação Máxima: {self.rmax} rpm\n Carga Máxima: {self.cargamax} Kg\n'

#Objetos
ddemon = Carro('dodge demon', 840, 1941.38, 6000, 7.05)
iron883 = Moto('harley davidson iron 883', 49, 256, 6000, 180)
bino = Caminhão('meu caminhão barbíssimo',2000, 3000, 2500, 15000)

veiculista = [ddemon, iron883, bino]
for veiculo in veiculista:
    print(veiculo)