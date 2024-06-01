# Para criar uma aplicação Tkinter básica, você precisa criar um objeto Tk,
# que representa a janela principal da aplicação.

import tkinter as tk

# Cria a janela principal
janela = tk.Tk()
janela.title("Minha primeira aplicação Tkinter")

# Inicia o loop principal da aplicação
janela.mainloop()

# Widgets Basicos

# widgets mais comuns incluem Label, 
# Button, Entry (campo de texto), Text (área de texto), Frame (contêiner), Canvas, e Listbox

# LABEL Um Label é usado para exibir texto ou imagens.
import tkinter as tk

janela = tk.Tk()
janela.title("Label Example")

# Cria um label
label = tk.Label(janela, text="Olá, Tkinter!")
label.pack()  # Adiciona o label à janela

janela.mainloop()

# BUTTON Um Button é usado para executar uma ação quando clicado.
import tkinter as tk

def clique():
    print("Botão clicado!")

janela = tk.Tk()
janela.title("Button Example")

# Cria um botão
botao = tk.Button(janela, text="Clique aqui", command=clique)
botao.pack()

janela.mainloop()

# ENTRY Um Entry é um campo de entrada de texto.
import tkinter as tk

janela = tk.Tk()
janela.title("Entry Example")

# Cria um campo de entrada
entrada = tk.Entry(janela)
entrada.pack()

# Função para exibir o texto inserido
def mostrar_texto():
    print("Texto inserido:", entrada.get())

# Botão para exibir o texto inserido
botao = tk.Button(janela, text="Mostrar Texto", command=mostrar_texto)
botao.pack()

janela.mainloop()

# Layout
# Ajusta o layout dos Widgets dentro da janela

# PACK() O método pack() organiza os widgets em blocos antes de colocá-los na janela.
import tkinter as tk

janela = tk.Tk()
janela.title("Pack Layout Example")

label1 = tk.Label(janela, text="Label 1")
label1.pack(side=tk.LEFT)  # Organiza à esquerda

label2 = tk.Label(janela, text="Label 2")
label2.pack(side=tk.RIGHT)  # Organiza à direita

janela.mainloop()

# GRID() O método grid() organiza os widgets em uma grade.
import tkinter as tk

janela = tk.Tk()
janela.title("Grid Layout Example")

label1 = tk.Label(janela, text="Label 1")
label1.grid(row=0, column=0)

label2 = tk.Label(janela, text="Label 2")
label2.grid(row=0, column=1)

label3 = tk.Label(janela, text="Label 3")
label3.grid(row=1, column=0, columnspan=2)  # Ocupa duas colunas

janela.mainloop()

# PLACE() O método place() posiciona os widgets em coordenadas absolutas ou relativas dentro da janela
import tkinter as tk

janela = tk.Tk()
janela.title("Place Layout Example")

label1 = tk.Label(janela, text="Label 1")
label1.place(x=50, y=50)  # Posição absoluta

label2 = tk.Label(janela, text="Label 2")
label2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Posição relativa

janela.mainloop()

# Ligando Funções
# Tkinter é baseado em eventos. 
# Isso significa que você pode ligar funções (callbacks) a eventos, como cliques de botão ou teclas pressionadas.

import tkinter as tk

def tecla_pressionada(event):
    print(f"Tecla pressionada: {event.char}")

janela = tk.Tk()
janela.title("Event Example")

# Liga o evento de tecla pressionada à janela
janela.bind("<Key>", tecla_pressionada)

janela.mainloop()

# Para aplicações Complexas
# Para aplicações mais complexas, é útil organizar seu código em classes.

import tkinter as tk

class MinhaAplicacao(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicação Tkinter com Classes")
        
        self.label = tk.Label(self, text="Olá, Tkinter!")
        self.label.pack()
        
        self.botao = tk.Button(self, text="Clique aqui", command=self.clique)
        self.botao.pack()
    
    def clique(self):
        self.label.config(text="Botão clicado!")

if __name__ == "__main__":
    app = MinhaAplicacao()
    app.mainloop()

    