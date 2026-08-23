# 22. Desenvolva uma versão da busca binária que encontre a primeira ocorrência de um valor repetido em uma lista ordenada.
import random

def busca_binaria(lista, valor):
    pos_ini = 0
    pos_fim = len(lista)-1
    apari = -1

    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2

        if lista[pos_meio] == valor:
            apari = pos_meio
            pos_fim = pos_meio -1
        elif lista[pos_meio] > valor:
            pos_fim = pos_meio -1
        else:
            pos_ini = pos_meio + 1
    return apari

lista = [random.randint(0,10) for i in range(0,10)]
lista = sorted(lista)

n = random.randint(1,10)
res = busca_binaria(lista, n)
print(f'Lista: {lista}')
if res == -1:
    print(f'Número {n} não encontrado.')
else:
    print(f'O número {n} está na posição {res}')