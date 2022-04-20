# vamos ver heranças


class Programa:
    def __init__(self, nome, lancamento):
        self._nome = nome.title() #Usar dois underlines faz do atributo privado, indica que ele não deve ser usado diretamente mas sim deve ser invocado através de uma def categorizada com o decorador @proprty que retorna o atributo secreto, a def pode ter o nome do atributo sem os underscores.
        self.lancamento = lancamento
        self._likes = 0 #Porém usa-se apenas um underline quando queremos indicar que um atributo é privado mas é herdado por outras classes (objetos), ou seja se uma classe for usadam como mãe, seus atributos privados devem ser acessados na criação de outros objetos, por isso um underline. Caso os dois underlines fossem mantiddos, classes filhas teriam que se referir a tal atributo como _[class name]__[atribute]

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novonome):
        self._nome = novonome

    @property
    def likes(self):
        return self._likes

    def darlike(self):
        self._likes += 1


class Filme(Programa):
    def __init__(self, nome, lancamento, duracao):
        super().__init__(nome, lancamento)
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, nome, lancamento, temporadas):
        super().__init__(nome, lancamento)
        self.temporadas = temporadas

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
blackmirror= Serie("Black mirros", 2015, 4)