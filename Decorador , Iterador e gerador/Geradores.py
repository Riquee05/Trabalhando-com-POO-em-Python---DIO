# Uma função geradora é definida como uma função normal, 
#mas usa a palavra-chave yield para retornar valores um de cada vez

# Eles permitem que você produza uma sequência de valores um de cada vez

def contador(maximo):
    atual = 0
    while atual < maximo:
        yield atual
        atual += 1

# Usando o gerador
for num in contador(5):
    print(num)  # 0, 1, 2, 3, 4

# Criando geradores com Expressões

quadrados = (x**2 for x in range(5))
for num in quadrados:
    print(num)  # 0, 1, 4, 9, 16

# Comparação entre Lista e Gerador

# Usando uma lista (armazena todos os valores na memória)
lista = [x**2 for x in range(1000)]
print(sum(lista))  # Soma de todos os quadrados

# Usando um gerador (produz valores um de cada vez)
gerador = (x**2 for x in range(1000))
print(sum(gerador))  # Soma de todos os quadrados


# Modulo Intertools

import itertools

# Contador infinito
contador = itertools.count(start=1, step=1)
for _ in range(5):
    print(next(contador))  # 1, 2, 3, 4, 5

# Ciclo infinito
ciclo = itertools.cycle('ABC')
for _ in range(5):
    print(next(ciclo))  # A, B, C, A, B


# Geradores aninhados

def gerador1():
    yield from range(3)
    
def gerador2():
    yield from gerador1()
    yield from range(3, 6)

for num in gerador2():
    print(num)  # 0, 1, 2, 3, 4, 5




