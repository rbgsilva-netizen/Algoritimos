# 24. Dada uma lista ordenada de idades, utilize busca binária para verificar se uma idade específica está presente
# e informe quantos elementos foram descartados durante o processo.

def busca_bin(lista, valor):
    pos_ini = 0
    pos_fim = len(lista) - 1
    descartes = 0
    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2

        if lista[pos_meio] == valor:
            return True, descartes
        elif lista[pos_meio] > valor:
            descartes += (pos_fim - pos_meio) + 1
            pos_fim = pos_meio - 1
        else:
            descartes += (pos_meio - pos_ini) + 1
            pos_ini = pos_meio +1
    return False, descartes


lista = [0,1,2,3,4,5,6,7,8,9,10]
n = int(input('Digite um número: '))

resultado, descartes = busca_bin(lista, n)

if resultado:
    print(f'Após {descartes} descartes, o número {n} foi encontrado!')
else:
    print(f'Após {descartes} descartes, o número {n} não foi encontrado!')