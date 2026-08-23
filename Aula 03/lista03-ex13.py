# 13. Crie uma lista ordenada de números inteiros e implemente manualmente a busca binária para localizar um número informado pelo usuário.


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


lista = [10,11,12,13,14,15,16,17,18,19,20]
busca = int(input('Busque um valor na lista: '))
resultado = busca_binaria(lista, busca)

if resultado == -1:
    print('Valor não encontrado')
else:
    print(f'Valor encontrado na posição {resultado}')
