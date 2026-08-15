# 18. Frequência dos elementos
# Dada uma lista de números inteiros, informe quantas vezes cada valor aparece.
# Exemplo: para [2, 3, 2, 5, 3, 2], a saída deve indicar que 2 aparece 3 vezes, 3 aparece 2 vezes e 5 aparece 1 vez.
import random

lista = []
lista2 = []

for i in range(10):
    lista.append(random.randint(1,10))
print(f'Lista: {lista}')

for i in lista:
    cont = 0
    if i not in lista2:
        lista2.append(i)
        for j in lista:
            if j == i:
                cont += 1
        print(f'O número {i} aparece {cont}x na lista')