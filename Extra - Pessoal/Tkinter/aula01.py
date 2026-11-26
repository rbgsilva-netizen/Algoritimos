import tkinter as tk


#Janela principal
janela = tk.Tk()

#configurando a janela
janela.title("minha primeira aplicação")
janela.geometry("400x250")


# Função executada pelo botão
def cumprimentar():
    nome = entrada.get()
    resultado.config(text=f"Olá, {nome}!")

# Texto
titulo = tk.Label(
    janela,
    text="Digite seu nome:"
)
titulo.pack(pady=10)

# Campo de entrada
entrada = tk.Entry(janela)
entrada.pack()

# Botão
botao = tk.Button(
    janela,
    text="Enviar",
    command=cumprimentar
)
botao.pack(pady=10)

# Resultado
resultado = tk.Label(janela,text="")
resultado.pack()


#Mantém a janela aberta
janela.mainloop()