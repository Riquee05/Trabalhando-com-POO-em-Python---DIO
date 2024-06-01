# Eles são usados para "decorar" uma função com funcionalidades adicionais, sem modificar seu código. 
# Aqui está um resumo fácil sobre como usar decoradores:

#Simples
def meu_decorador(func):
    def wrapper():
        print("Algo acontece antes da função ser chamada.")
        func()
        print("Algo acontece depois da função ser chamada.")
    return wrapper

@meu_decorador
def diz_ola():
    print("Olá!")

diz_ola()

# Com Argumentos

def meu_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes da função ser chamada.")
        resultado = func(*args, **kwargs)
        print("Depois da função ser chamada.")
        return resultado
    return wrapper

@meu_decorador
def soma(a, b):
    return a + b

print(soma(3, 4))

# Com Argumentos personalizados

def repeticoes(n):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorador

@repeticoes(3)
def diz_ola():
    print("Olá!")

diz_ola()

# Decoradores de Metodos
# Decoradores também podem ser usados em métodos de classes.

def meu_decorador(func):
    def wrapper(self, *args, **kwargs):
        print("Antes do método ser chamado.")
        resultado = func(self, *args, **kwargs)
        print("Depois do método ser chamado.")
        return resultado
    return wrapper

class MinhaClasse:
    @meu_decorador
    def meu_metodo(self):
        print("Método sendo chamado.")

obj = MinhaClasse()
obj.meu_metodo()

#Utilizando functools.wraps
# Para preservar informações da função original (como nome, docstring), 
# é uma boa prática usar functools.wraps no decorador.

import functools

def meu_decorador(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Antes da função.")
        resultado = func(*args, **kwargs)
        print("Depois da função.")
        return resultado
    return wrapper

@meu_decorador
def diz_ola():
    """Diz Olá"""
    print("Olá!")

print(diz_ola.__name__)  # diz_ola
print(diz_ola.__doc__)   # Diz Olá
