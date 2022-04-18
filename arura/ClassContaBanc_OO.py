# Essa conta possui proteção contras atualização direta de salado
from datetime import datetime

class user:

    def __init__(self, nome, conta):
        self.nome = nome
        self.__conta = conta #atributo se torna inacessível diretamente pela classe, é necessário a criação de uma def capaz de printar esse atributo
        self.__data_criacao = datetime.now()
        self.__limite = float(1000)
        self.__saldo = float(0)
        self.__interops = False
        self.extrato = {} #Nesse caso o extarto é contínuo, com a key evidenciando o tipo da movimentação ("Depósito...", "Saldo...").Talvez num próximo momento será feito um nested dictionary onde haverá dois diferentes dicts, um com todos os depósitos e um com os saldos.
        print('Conta configurada com sucesso {}'.format(self.nome))

    @property
    def conta(self):
        return self.__conta

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, novosaldo):
        if self.__interops:
            self.__saldo = float(novosaldo)
        else:
            print('\n*** Ação Proibida, sua tentativa foi catalogada em nosso banco de dados ***\n')

    def deposito(self, valor):
        self.__interops = True
        self.saldo = self.saldo + abs(valor)
        self.__interops = False
        self.extrato['Depósito {}'.format(datetime.now())] = "R${:.2f}".format(float(abs(valor)))
        print('Depósito de {:.2f} feito com sucesso, para {}'.format(float(valor), self.nome))

    def saque(self, valor):
        if self.saldo-abs(valor)>=-self.limite:
            self.__interops = True
            self.saldo = self.saldo - abs(valor)
            self.__interops = False
            self.extrato['Saque {}'.format(datetime.now())] = "R${:.2f}".format(float(abs(valor)))
            print('Saque de {:.2f} feito com sucesso, de {}'.format(float(valor), self.nome))
        else:
            print('Esse saque ultrapassa seu limite de -R${}, levando seu saldo final a: R${:.2f}\nSaque não efetuado'.format(self.limite, float(self.saldo-abs(valor))))

    def print_saldo(self):
        print('Saldo atual de R${:.2f}'.format(self.saldo))
    
    def transferencia(self, valor, destino):
        self.saque(abs(valor))
        destino.deposito(valor)
        print('R${:.2f} foram transferidos de {} para {}'.format(float(valor), self.nome, destino.nome))

    def get_saldo(self):
        return "RS {:.2f}".format(self.saldo)   
    
    def get_extrato(self):
        return self.extrato

    @property #limite foi settado como um atributo oculto, então cria-se uma def, catergorizando-a como propriedade da classe com @property, com nome limite. Caso seja invocada, mostra o limite, caso seja atribuido um valor, altera-se o valor de limite que pr fim altera o valor de __limite
    def limite(self):
        # print('Seu limite é de R${:.2f}'.format(self.__limite))
        return self.__limite

    @limite.setter
    def limite(self, novolimite):
        self.__limite = abs(float(novolimite))
        print('Limite alterado para R${:.2f}'.format(abs(float(novolimite))))