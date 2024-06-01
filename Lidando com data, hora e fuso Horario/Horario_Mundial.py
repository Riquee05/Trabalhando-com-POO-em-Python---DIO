
# Exemplo de como Usar o Tkinter com Datetime

import tkinter as tk
from datetime import datetime

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Exibição de Data e Hora")
        root.configure(background="gray")

        self.label = tk.Label(root, text="", font=("Arial", 48))
        self.label.pack(pady=20)

        self.atualizar_hora()

    def atualizar_hora(self):
        now = datetime.now()
        hora_atual = now.strftime("%Y-%m-%d %H:%M:%S")
        self.label.config(text=hora_atual)
        self.root.after(1000, self.atualizar_hora)  # Atualiza a cada segundo
        root.configure(background="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
