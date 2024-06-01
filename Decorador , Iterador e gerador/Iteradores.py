# Iteradores em Python são objetos que permitem percorrer todos os elementos de uma coleção (como listas, tuplas, dicionários, etc.) de forma sequencial. 
#Eles são uma parte fundamental do protocolo de iteração do Python. 
#Aqui está um resumo fácil sobre como trabalhar com iteradores:

# Conceito Basico

# Um objeto é iterável se pode ser passado para a função iter(), que retorna um iterador. 
#Exemplos de objetos iteráveis são listas, tuplas, strings e dicionários.

lista = [1, 2, 3]
iterador = iter(lista)
print(iterador)  # <list_iterator object at 0x...>

#Um iterador é um objeto com o método __next__() 
#que retorna o próximo elemento da coleção quando chamado. Quando não há mais elementos, 
#levanta a exceção StopIteration.

iterador = iter(lista)
print(next(iterador))  # 1
print(next(iterador))  # 2
print(next(iterador))  # 3
# print(next(iterador))  # StopIteration

# Criando Iteradores Personalizados

# Você pode criar um iterador personalizado definindo uma classe com os métodos __iter__() e __next__().

class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.atual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual < self.limite:
            self.atual += 1
            return self.atual
        else:
            raise StopIteration

contador = Contador(5)
for numero in contador:
    print(numero)

# Usando Funções integradas

# MAP() Aplica uma função a todos os itens em um iterável.

numeros = [1, 2, 3, 4]
quadrados = map(lambda x: x**2, numeros)
print(list(quadrados))  # [1, 4, 9, 16]

# FILTER() Filtra itens em um iterável com base em uma função.

numeros = [1, 2, 3, 4]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # [2, 4]

# ZIP() Combina vários iteráveis elemento por elemento

a = [1, 2, 3]
b = ['um', 'dois', 'três']
combinado = zip(a, b)
print(list(combinado))  # [(1, 'um'), (2, 'dois'), (3, 'três')]

# ITERTOOLS O módulo itertools oferece funções que criam iteradores para tarefas de iteração complexas.

import itertools

# Contador infinito
contador = itertools.count(start=1, step=2)
for _ in range(5):
    print(next(contador))  # 1, 3, 5, 7, 9

# Permutações
permutacoes = itertools.permutations('ABC')
print(list(permutacoes))  # [('A', 'B', 'C'), ('A', 'C', 'B'), ...]

# Combinações
combinacoes = itertools.combinations('ABC', 2)
print(list(combinacoes))  # [('A', 'B'), ('A', 'C'), ('B', 'C')]
