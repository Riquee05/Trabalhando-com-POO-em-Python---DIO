# metodos Abstrato não tem corpo, porem todas as classes filhas são obrigadas a Usar
# Com metodos abstratos, as classes viram Abstratas, e não consigo instancia-las diretamente

# ABC abstract based class, para usa-lo:

# O From importa dos modulos, as classes, no caso o From importa do Modulo abc a classe ABC
from abc import ABC, abstractmethod, abstractproperty

class controleRemoto(ABC): # Extendo o ABC para a classe virar abstrata e fazer com que ControleTV tenha metodos obrigatorios
    @abstractmethod # Definindo os metodos como Abstratos
    def ligar(self): # contrato(ligar, não recebe argumento)
        pass

    @abstractmethod
    def desligar(self): # contrato(desligar, não recebe argumento)
        pass

    @property
    @abstractproperty
    def marca(self): # Para forçar todas as classes filhas a terem uma propriedade, no exemplo Marca
        pass


# Se extender de controle remoto, posso estanciar os metodos da classe em minha classe ControleTV
# e instancia-los
class controleTv(controleRemoto): 
    # para instanciar, precisa-se ultilizar os metodos da classe abstrata (ControleRemoto)
    def ligar(self):
        print("Ligando a TV")
        print("Ligada")

    def desligar(self):
        print("Desligando a TV")
        print("Desligada") 

    
    

class arCondicionado(controleRemoto): #Criada a classe Ar condicionado somente com o Metodo Ligar.

    # ira dar um erro ao executar o Codigo, pois é obrigado o uso de todos os metodos
    def ligar(self):
        print("Ligando o arCondicionado")
        print("ligado")        

   # def desligar(self):
       # print("Desligando o arCondicionado")
       # print("Desligado")



controle = controleTv()
controle.ligar()
controle.desligar()

controle = arCondicionado() # se eu não usar o metodo desligar, o codigo não ira pegar
controle.ligar()
# controle.desligar()