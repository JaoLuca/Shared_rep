class Mãe():
    def quem_sou_eu(self):
        return 'Eu sou a classe mãe, a superclass geral'
    pass

class Pai():
    def quem_sou_eu(self):
        return 'Eu fui comprar leite'
    pass    

class Filha(Mãe):
    def quem_sou_eu(self):
        return 'Eu sou a filha preferida da mãe'
    pass

class Filha2(Mãe):
    def quem_sou_eu(self):
        return 'Eu sou a filha 2 da mãe'
    pass

class Filha3(Mãe):
    def quem_sou_eu(self):
        return 'Eu sou a filha 3 da mãe'
    pass

class Filho(Pai):
    def quem_sou_eu(self):
        return 'Eu sou o filho do Pai'
    pass

class Filho2(Pai):
    def quem_sou_eu(self):
        return 'Eu sou o filho2 do Pai'
    pass

class Neto_Incestuoso(Filha, Filho, Filha2, Filha3, Filho2):
    def quem_sou_eu(self):
        return 'Sou neto da Mãe, filho dos filhos da mãe'
    pass



pirralho = Neto_Incestuoso()


#Ao chamar a função 'quem_sou_eu' o python vai atrás dessa função na classe com a qual o objeto foi instânciado

#No caso, o objeto pirralho tem a função quem_sou_eu() e retornará o valor dessa função, mas caso ela não esteja presente na classe Neto_incestuoso() o que acontecerá caso essa def seja chamada? a) Erro b)Procura essa def nas superclasses

#Ao achar a mesma função na superclasse (no caso a classe mãe imediata da classe neto é a Filha(), e se Filha() tiver a def quem_sou_eu() ela será executada.) a função quem_sou_eu() da superclasse imediata será executada.

#Mas e se a superclasse de Neto_Incestuoso(), no caso Filha(),  não possuir a def quem_sou_eu(), o que acontecerá?

#Ai o python tem um sistema de escolha interessante: Caso a superclass Filha() for a única superclass com supersuperclass Mãe(), ela será acessada prioritariamente à Filho(), agora caso a supersuperclass Mãe() ainda for supersuperclass de mais alguma superclass de Neto_Incestuoso() (no caso Mãe() é supersuperclass de Filha2() e Filha3()) ela ainda não será acessada (ainda não será "gasta") ja que ainda temos outras superclasses de Neto_Incestuoso() que a herdam. Ou seja, somente quando não houverem mais superclasses com supersuperclasses compartilhadas (herdam a mesma superclasse) que a supersuperclasse em questão será acessada para buscar a função de mesmo nome, no caso quem_sou_eu().

#Para testar isso va comentando as def quem_sou_eu() de cada classe, uma de cada vez e veja a frase printada, ai comente a def da frase pintuda para ver qual será a próxima a ser acessada.    
print(pirralho.quem_sou_eu())
