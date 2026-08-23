# 25. Sistema de Biblioteca: Uma biblioteca possui uma lista ordenada de códigos de livros.
# Implemente uma busca binária para verificar se um código informado está disponível.
# Caso esteja, informe a posição do livro na lista.


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

lista = [
    1001,
    1015,
    1023,
    1048,
    1056,
    1072,
    1089,
    1104,
    1120,
    1137,
    1153,
    1178,
    1201,
    1235,
    1260,
    1302,
    1347,
    1405,
    1450,
    1508
]

busca = int(input('Busque um livro pelo seu código: '))

res = busca_binaria(lista, busca)

if res == -1:
    print('O livro não está disponível.')
else:
    print(f'O livro está disponível no indice {res}')