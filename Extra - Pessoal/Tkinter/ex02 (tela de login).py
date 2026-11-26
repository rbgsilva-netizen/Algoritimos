import tkinter as tk

janela = tk.Tk()
janela.title("Sistema de Login")
janela.geometry("430x350")

usuario_correto = "admin"
senha_correta = "123"


def logarUsuario():
    lg = usuario.get()
    pw = senha.get()
    label_txt = ""
    label_cor = "black"

    if not lg or not pw:
        label_txt = "Preencha todos os campos!"
        label_cor = "red"
    elif lg == usuario_correto and pw == senha_correta:
        label_txt = "Login realizado com sucesso!"
        label_cor = "green"
    else:
        label_txt = "Usuário/senha inválidos!"
        label_cor = "red" 

    resultado.config(text=label_txt, foreground=label_cor)

def limparCampos():
    usuario.delete(0,tk.END)
    senha.delete(0,tk.END)
    resultado.config(text="")


frame1 = tk.Frame(janela)
frame1.pack(padx=5, pady=5, fill=tk.X)

frame2 = tk.Frame(janela)
frame2.pack(padx=5,pady=5)

frame3 = tk.Frame(janela)
frame3.pack(padx=5, pady=5)

#Titulo
tk.Label(frame1, text="Acesso ao Sistema").pack(pady=10)

#campos
tk.Label(frame2, text="Usuário").grid(row=0,column=0)
usuario = tk.Entry(frame2,)
usuario.grid(row=0, column=1)
tk.Label(frame2, text="Senha").grid(row=1,column=0)
senha = tk.Entry(frame2,show="*")
senha.grid(row=1, column=1)

resultado = tk.Label(frame2, text="")
resultado.grid(row=2, column=0, columnspan=2, padx=5,pady=5)

#botoes
entrar = tk.Button(frame3, text="Entrar", command=logarUsuario)
entrar.grid(row=0, column=0, padx=5)

limpar = tk.Button(frame3, text="Limpar", command=limparCampos)
limpar.grid(row=0, column=1, padx=5)

janela.mainloop()

