# 19. Implemente uma busca binária que retorne True ou False, sem retornar o índice do elemento.


def busca_binaria(lista, valor):
    pos_ini = 0
    pos_fim = len(lista)-1
    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2

        if lista[pos_meio] == valor:
            return True
        elif lista[pos_meio] > valor:
            pos_fim = pos_meio -1
        else:
            pos_ini = pos_meio + 1
    return False

lista = [i for i in 'abcdefghijklmnopqrstuvxz']
valor = '$'

resultado = busca_binaria(lista, valor)

if resultado:
    print('Valor encontrado.')
else:
    print('Valor não encontrado.')