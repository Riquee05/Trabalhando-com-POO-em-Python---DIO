class Carro: #Definimos a classe Carro

    #O propósito do __init__ é inicializar os atributos do objeto, ou seja, configurar o estado inicial do objeto
    def __init__(self, modelo,cor,ano,valor): #Iniciamos a Função de inicializar(metodo Construtor)
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor


    #Definindo Funções da classe Carro
    def ligar(self): 
        print("Colocar a chave no contato")
        print("pisar na embreagem")
        print("Colocar o cambio em Ponto morto")
        print("girar a chave")

    def andar(self):
        print("pisar na embreagem")
        print("engatar a primeira")
        print("acelerar e soltar a embreagem")

    def desligar(self):
        print("pisar na embreagem")
        print("colocar o cambio em ponto morto")
        print("girar a chave e tirar do contato")

    #Criando uma Função para retornar as informações do Objeto de uma maneira completa
    # o f antes da String permite que eu coloque os valores de expressões e variaveis dentro de chaves {}, exemplo abaixo
    def __str__(self):
        return f" \n Carro: Modelo = {self.modelo}, Cor = {self.cor}, ano = {self.ano}, valor = {self.valor} "
    
#Criando uma nova Instancia da Classe "Carro"
carro1 = Carro ("Meriva" , "Prata" , 2006 , 15000.0)
carro2 = Carro ("City" , "Preto" , 2013 , 65000.0)


# Acessando os atributos do Objeto
carro1.ligar()
carro1.andar()
carro1.desligar()
print(carro1)
