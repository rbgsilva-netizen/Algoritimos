import tkinter as tk

janela = tk.Tk()
janela.title("Exercício 01")
janela.geometry("500x350")


def apresentar():
    nome = entrada.get()
    resultado.config(text=f"Olá, {nome}.")


titulo = tk.Label(janela,text="Bem-vindo ao Tkinter!")
titulo.pack(pady=10)

entrada = tk.Entry(janela)
entrada.pack()

botao = tk.Button(janela, text="Apresentar", command=apresentar)
botao.pack(pady=10)

resultado = tk.Label(janela,text="")
resultado.pack()

janela.mainloop()