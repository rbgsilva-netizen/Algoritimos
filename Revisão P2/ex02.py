# Problema 2 — Organização de produtos de uma loja
# Uma loja deseja apresentar os preços de seus produtos em ordem crescente para facilitar a consulta dos clientes.
# Desenvolva um programa que:
# 1. Armazene pelo menos 8 preços em uma lista.
# 2. Crie a função bubble_sort(lista) para ordenar os preços.
# 3. Implemente o Bubble Sort com dois laços e comparação entre elementos vizinhos.
# 4. Mostre a lista antes e depois da ordenação.
# 5. Conte e apresente o número de comparações e trocas realizadas.


import random

precos = [random.randint(1,100) for i in range(8)]

def bubblesort(lista):
    comparacoes = 0
    trocas = 0
    n = len(lista)
    for i in range(n-1):
        trocou = False
        for j in range(n-i-1):
            comparacoes += 1
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
                trocas += 1
                
        if not trocou:
            break

    return lista, comparacoes, trocas


precos2, comparacoes, trocas = bubblesort(precos.copy())

print('-'*70)
print(f'Lista de preços antes da ordenação: {precos}')
print(f'Lista de precos depois da ordenação {precos2}')
print(f'Número de iterações: {comparacoes}')
print(f'Número de trocas: {trocas}')
print('-'*70)