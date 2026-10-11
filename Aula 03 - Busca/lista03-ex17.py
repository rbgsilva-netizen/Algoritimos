# 17. Dada uma lista ordenada de códigos de produtos, solicite um código e utilize busca binária para verificar se ele está cadastrado.

def busca_binaria(lista, valor):
    posIni = 0
    posFim = len(lista) - 1
    while posIni <= posFim:
        posMeio = (posIni + posFim) // 2

        if lista[posMeio] == valor:
            return posMeio
        elif lista[posMeio] > valor:
            posFim = posMeio - 1
        else:
            posIni = posMeio + 1
    return -1

lista = [
    1001,
    1005,
    1012,
    1020,
    1034,
    1041,
    1050,
    1067,
    1075,
    1083,
    1090,
    1102,
    1115,
    1128,
    1140,
    1156,
    1170,
    1184,
    1200,
    1215
]

busca = int(input('Digite o código do produto a ser pesquisado: '))
result = busca_binaria(lista, busca)

if result == -1:
    print('Código não encontrado.')
else:
    print(f'O código {busca} está cadastrado na posição {result}')