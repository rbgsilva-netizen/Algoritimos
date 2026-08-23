# 21. Crie uma lista ordenada com valores repetidos.
# Implemente uma busca binária capaz de localizar uma ocorrência do valor procurado e informe seu índice.
import random

def busca_binaria(lista, valor):
    pos_ini = 0
    pos_fim = len(lista)-1
    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2

        if lista[pos_meio] == valor:
            return pos_meio
        elif lista[pos_meio] > valor:
            pos_fim = pos_meio -1
        else:
            pos_ini = pos_meio + 1
    return -1

lista = [random.randint(0,10) for i in range(0,20)]
lista = sorted(lista)
n = 5
res = busca_binaria(lista, n)
print(f'Lista: {lista}')
if res == -1:
    print('Número não encontrado.')
else:
    print(f'O número {n} está na posição {res}')