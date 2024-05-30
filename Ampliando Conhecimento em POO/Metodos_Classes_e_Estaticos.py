# Metodos de classe estão ligados a Classe e não ao Objeto, eles tem acesso ao estado da classe,
# Pois recebem um parametro que aponta para a Classe e não para a instancia do Objeto

class pessoa:

    def __init__(self,  nome , idade):
        self.nome = nome
        self.idade = idade

    @classmethod # Criar um metodo de class, chama-se o @classmethod
    def criar_de_data_nascimento (cls , ano , mes ,dia , nome): # Usa-se o cls em vez de Self, o cls é uma instancia
        idade = 2024 - ano
        return pessoa(nome , idade)
    
# Sem metodo de classe, cria -se uma instancia

p1 = pessoa("Henrique", 25)
print(p1.nome , p1.idade)

# Com metodo de Classe, não precisa instanciar, o CLS puxa a classe pessoa e implementa o metodo
    
p = pessoa.criar_de_data_nascimento(1999,5,8,"Henrique")
print(p.nome, p.idade)

#Metodo estatico não recebe um primeiro Argumento explicito, ele tambem é um metodo ligado a classe,
# e não ao Objeto da classe, esse metodo não pode acessar ou modificar o estado da Classe.
# Ele esta presente em uma classe pois faz sentido que o metodo esteja presente na classe.

    
    
@staticmethod # Criar um metodo de class, chama-se o @staticmethod
def e_maior_idade(idade):
    return idade > 18

pessoa.e_maior_idade(18)
pessoa.e_maior_idade(28)

# Eu preciso de um metodo com acesso ao contexto da classe, eu uso o Metodo de classe
# Eu não preciso da classe, nem da instancia do Objeto, eu uso o Metodo estatico