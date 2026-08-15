# 17. Segundo maior valor
# Dada uma lista de números inteiros, encontre o segundo maior valor distinto sem utilizar sort().
# Considere que a lista possui pelo menos dois valores distintos.
import random

# cria a lista
lista = []
for i in range(10):
    lista.append(random.randint(1,50))
print(f'Lista Inicial: {lista}')

# ordena a lista
c = len(lista)
for i in range(c):
    for j in range(0,c-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
print(f'Lista ordenada sem função sort: {lista}')

# acha o segundo maior
while lista[-1] == lista[c-2]:
    c -= 1
print(f'O segundo maior valor da lista é: {lista[c-2]}')