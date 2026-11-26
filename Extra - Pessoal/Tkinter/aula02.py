import tkinter as tk

janela = tk.Tk()
janela.title("Aula 02")
janela.geometry("400x400")


# .pack() --------------------------------------------------------------------
# tk.Label(janela, text="Superior").pack(side=tk.TOP)
# tk.Label(janela, text="Inferior").pack(side=tk.BOTTOM)
# tk.Label(janela, text="Esquerda").pack(side=tk.LEFT)
# tk.Label(janela, text="Direita").pack(side=tk.RIGHT)

# tk.Button(janela,text="Espaço Externo").pack(padx=20, pady=10)
# tk.Button(janela,text="Espaço Interno").pack(ipadx=20, ipady=10)

# tk.Button(janela,text="Fill tk.X").pack(fill=tk.X)
# tk.Button(janela,text="Fill tk.y").pack(fill=tk.Y)
# tk.Button(janela,text="Fill tk.both").pack(fill=tk.BOTH, expand=True)


# # .grid() --------------------------------------------------------------------
tk.Label(janela, text="Nome").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(janela).grid(row=0, column=1, padx=10, pady=10)

tk.Label(janela, text="Idade").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(janela).grid(row=1, column=1, padx=10, pady=10)

tk.Button(janela,text="Cadastrar").grid(row=2,column=0, columnspan=2, padx=5, pady=10, sticky="ew")


# # .place() --------------------------------------------------------------------
tk.Label(janela, text="place(x=250, y=50)").place(x=250, y=50)
tk.Label(janela, text="place(relx=0.5, rely=0.5, anchor='center')").place(relx=0.5, rely=0.5, anchor="center")










janela.mainloop()