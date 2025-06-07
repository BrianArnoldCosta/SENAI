from os import system as limp
limp("cls")

import tkinter as tk
import math

class CalculadoraCientifica:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Científica")

        self.ligada = False
        self.historico = []

        self.display = tk.Entry(master, width=30, borderwidth=5, font=("Arial", 14))
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        self.criar_botoes()

    def ligar(self):
        self.ligada = True
        self.display.delete(0, tk.END)
        self.display.insert(0, "Ligada")

    def desligar(self):
        self.ligada = False
        self.display.delete(0, tk.END)
        self.display.insert(0, "Desligada")

    def inserir(self, valor):
        if self.ligada:
            atual = self.display.get()
            if atual in ["Ligada", "Desligada"]:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(valor))
            else:
                self.display.insert(tk.END, str(valor))

    def limpar(self):
        if self.ligada:
            self.display.delete(0, tk.END)

    def calcular(self):
        if self.ligada:
            try:
                expressao = self.display.get()
                resultado = eval(expressao, {"__builtins__": None}, vars(math))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(resultado))
                self.historico.append(f"{expressao} = {resultado}")
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Erro")

    def mostrar_historico(self):
        if self.ligada:
            self.display.delete(0, tk.END)
            historico_texto = "\n".join(self.historico[-5:])  # mostra os últimos 5
            self.display.insert(0, historico_texto)

    def criar_botoes(self):
        botoes = [
            ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3), ('sin',1,4),
            ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3), ('cos',2,4),
            ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3), ('log',3,4),
            ('0',4,0), ('.',4,1), ('+',4,2), ('sqrt',4,3), ('^',4,4),
            ('C',5,0), ('=',5,1), ('Hist',5,2), ('Ligar',5,3), ('Desligar',5,4)
        ]

        for (texto, linha, coluna) in botoes:
            if texto == '=':
                cmd = self.calcular
            elif texto == 'C':
                cmd = self.limpar
            elif texto == 'Hist':
                cmd = self.mostrar_historico
            elif texto == 'Ligar':
                cmd = self.ligar
            elif texto == 'Desligar':
                cmd = self.desligar
            elif texto == 'sqrt':
                cmd = lambda t='math.sqrt(': self.inserir(t)
            elif texto == 'sin':
                cmd = lambda t='math.sin(': self.inserir(t)
            elif texto == 'cos':
                cmd = lambda t='math.cos(': self.inserir(t)
            elif texto == 'log':
                cmd = lambda t='math.log(': self.inserir(t)
            elif texto == '^':
                cmd = lambda t='**': self.inserir(t)
            else:
                cmd = lambda t=texto: self.inserir(t)

            tk.Button(self.master, text=texto, width=8, height=2, command=cmd).grid(row=linha, column=coluna, padx=2, pady=2)


# Criar janela principal
root = tk.Tk()
app = CalculadoraCientifica(root)
root.mainloop()
