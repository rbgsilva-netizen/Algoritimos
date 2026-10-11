# 18. Modifique a busca binária para contar quantas comparações são necessárias para localizar um elemento.
import random

def busca_binaria(lista, valor):
    pos_ini = 0
    pos_fim = len(lista)-1
    c = 0
    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2
        c += 1

        if lista[pos_meio] == valor:
            return c
        elif lista[pos_meio] > valor:
            pos_fim = pos_meio -1
        else:
            pos_ini = pos_meio + 1
    return c


lista = [0,1,2,3,4,5,6,7,8,9,10]
n = random.randint(0,10)
comparacoes = busca_binaria(lista, n)

print(f'Comparações até encontrar o número {n}: {comparacoes}')

