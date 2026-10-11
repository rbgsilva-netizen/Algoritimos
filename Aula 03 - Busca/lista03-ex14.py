# 14. Crie uma função busca_binaria(lista, valor) que receba uma lista ordenada e retorne o índice do valor procurado
# ou -1 caso ele não seja encontrado.
import random

def busca_binaria(lista, valor):
    pos_ini = 0
    pos_fim = len(lista) - 1
    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2

        if lista[pos_meio] == valor:
            return pos_meio
        elif lista[pos_meio] > valor:
            pos_fim = pos_meio - 1
        else:
            pos_ini = pos_meio + 1
    return -1

lista = [random.randint(1,30) for _ in range(25)]
lista = sorted(lista)

busca = int(input('Encontre um valor na lista: '))
resultado = busca_binaria(lista, busca)

print(f'Lista: {lista}')
if resultado != -1:
    print(f'Valor encontrado na posição {resultado}.')
else:
    print('Valor não encontrado.')