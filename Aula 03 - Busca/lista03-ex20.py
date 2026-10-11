# 20. Dada uma lista ordenada contendo números pares de 2 até 200, utilize busca binária para localizar um número informado pelo usuário.

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


lista = [i for i in range(1,201) if i % 2 == 0]
n = int(input('Busque a posição de um número par entre 2 e 200: '))
res = busca_binaria(lista, n)

if res != -1:
    print('Posição:', res)
else:
    print(f'{n} não está na lista de pares entre 2 e 200.')