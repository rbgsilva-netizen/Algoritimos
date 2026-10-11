# 3. Crie uma função busca_sequencial(lista, valor) que retorne o índice do valor procurado ou -1 caso ele não esteja presente.
import random

def busca_sequencial(lista, valor):
    for k,v in enumerate(lista):
        if v == valor:
            return k
    return -1

lista = [random.randint(1,20) for i in range(15)]
print(f'Lista: {lista}')

busca = busca_sequencial(lista,9)
print(busca)