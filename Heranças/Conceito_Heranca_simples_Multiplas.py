# Herança Simples, quando uma classe filha, herda apenas uma classe Pai

# Herança Multipla, quando uma classe filha, herda de varias classes pai
# Ou ex. Classe avo, as classes pai herdam das classes avos e as classes filhas das classes pai

# Sintaxe Herança simples

class veiculo:
    def __init__(self, cor, placa, nro_rodas):
        self.cor = cor
        self.placa = placa
        self.nro_rodas = nro_rodas

    def ligando_motor(self):
          print("Ligando o Motor")

class motocicleta(veiculo):# Não precisamos colocar o Construtor nas classes filhas, pois herdam da classe Pai
        pass

class carro(veiculo):
        pass

class caminhao(veiculo): #Conseguimos adicionar novos metodos nas classes, sem influenciar nas outras 
    def carregado(self):
          print("Não esta carregado")

moto = motocicleta("Azul", "abc-1234", 2)
moto.ligando_motor()

carro = carro("Prata", "bcd-4569", 4)
carro.ligando_motor()

caminhao = caminhao("Preto", "hen-8988", 8)
caminhao.ligando_motor()
caminhao.carregado()

#Sintaxe Herança Multipla

class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)


gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)