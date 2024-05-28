# Atributo de Instancia, é proprio para cada Objeto, se eu trocar o Valor de uma instancia de um objeto,
# ele não vai influenciar os outros Objetos, pois é unico de cada Objeto

# Quando troca-se um valor de uma variavel dentro de uma Classe, automaticamente, 
# todos os Objetos passarão a ter o mesmo Valor

class Estudante:
    escola = "DIO" # Se trocar o Nome de escola, automaticamente todos os Objetos seguirão com o mesmo nome

    def __init__(self , nome , matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(* objs):
    for obs in objs:
        print(obs)

aluno_1 = Estudante ("Henrique" , 1) # Atribuido como Matricula 1
aluno_2 = Estudante ("Gabriel" , 2)
mostrar_valores (aluno_1 , aluno_2)

aluno_1.matricula = 3 # Se trocar o valor da instancia, somente a instancia seguira com esse valor, 
                      # Sem alterar nada das outras