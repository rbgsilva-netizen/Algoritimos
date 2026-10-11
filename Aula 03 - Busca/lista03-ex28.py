# 28. Comparação de Desempenho: Crie uma lista ordenada com 1.000 números.
# Procure o último elemento usando busca sequencial e busca binária.
# Conte o número de comparações realizadas em cada algoritmo e apresente uma conclusão.

def busca_seq(lista, valor):
    c = 0
    for k,v in enumerate(lista):
        c += 1
        if v == valor:
            return c
    return c

def busca_bin(lista,valor):
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

lista = []
for i in range(1000):
    lista.append(i)
n = lista[-1]

cont_seq = busca_seq(lista, n)
cont_bin = busca_bin(lista, n)

print(f'Contagem na busca sequencial: {cont_seq}')
print(f'Contagem na busca Binária: {cont_bin}')
print(f'A Contagem na busca binária realizou {cont_seq/cont_bin:.0f}x menos comparações')