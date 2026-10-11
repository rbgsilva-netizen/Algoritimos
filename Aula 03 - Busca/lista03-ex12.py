# 12. Implemente uma busca sequencial que pare assim que encontrar o valor procurado.
# Exiba o valor encontrado, sua posição e o número de comparações realizadas.


def buscaSeq(lista, valor):
    comparacoes = 0
    for k, v in enumerate(lista):
        comparacoes += 1
        if v == valor:
            return True, k, comparacoes
    return False, -1, comparacoes

lista = [10,9,8,7,6,5,4,3,2,1,0]

busca = int(input('Busque um valor na lista: '))

status, indice, comparacoes = buscaSeq(lista,busca)

if status:
    print(f'O número {busca} foi encontrado na posição {indice} após {comparacoes} comparações.')
else:
    print(f'Após {comparacoes} comparações, o número {busca} não foi encontrado.')