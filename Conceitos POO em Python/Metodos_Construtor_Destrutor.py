class cons_des:

#Metodo __Init__ Metodo construtor de uma classe, O propósito do __init__ é inicializar os atributos do objeto, 
# ou seja, configurar o estado inicial do objeto quando ele é instanciado.
    def __init__(self, new_metodo):

        self.new_metodo = new_metodo


# Metodo __del__ Metodo destrutor de uma classe,O propósito do __del__ é permitir que você execute qualquer limpeza final necessária, 
# como liberar recursos externos (arquivos, conexões de rede, etc.) antes que o objeto seja removido da memória.
    def __del__(self):

        pass