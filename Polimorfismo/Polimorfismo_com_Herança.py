# O conceito de herança continua o mesmo (Classes filhas Herdam classes pai), no polimorfismo com herança
# o conceito continua o mesmo, é criado um metodo onde eu consigo pegar e executar as duas classes Ex.

class passaro: # Classe Pai
    def voar(self): pass

class pardal(passaro): #Classe filha herda classe pai
    print("O pardal voa")

class avestruz(passaro): #Classe filha herda classe pai
    print("O avestruz não voa")

def plano_de_voo(passaro): # Criada uma função onde pede o Objeto (passaro) mas pode ser qualquer nome e cria uma dunção passaro.voar
    passaro.voar()

plano_de_voo(pardal())
plano_de_voo(avestruz())