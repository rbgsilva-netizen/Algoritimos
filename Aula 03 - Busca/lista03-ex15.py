# 15. Dada uma lista ordenada de nomes, implemente uma busca binária para verificar se um nome informado pelo usuário está presente na lista.

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
    "Ana",
    "Bruno",
    "Carlos",
    "Daniela",
    "Eduardo",
    "Fernanda",
    "Gabriel",
    "Helena",
    "Igor",
    "Juliana",
    "Lucas",
    "Mariana",
    "Pedro",
    "Rafael",
    "Sofia"
]

busca = input('Verifique se um nome está cadastrado: ').title()
result = busca_binaria(lista, busca)

if result == -1:
    print('Nome não encontrado.')
else:
    print(f'O nome {busca} está cadastrado na posição {result}')