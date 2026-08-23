# 2. Dada uma lista de nomes, solicite um nome ao usuário e utilize a busca sequencial para informar a posição em que ele foi encontrado.
# Caso não exista, informe uma mensagem adequada.

def busca_seq(lista,valor):
    n = len(lista)
    for i in range(n):
        if lista[i] == valor:
            return f'O nome {valor} está na posição {i} da lista.'
    return f'O nome {valor} não está na lista.'



lista = ['Ricardo','Fernando','Alexsander','Bernardo','Caio','Micael','João','Roger']

nome = input("Busque um nome da lista: ").title()
busca = busca_seq(lista,nome)
print(busca)