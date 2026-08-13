# 5. Maior e menor valor
# Crie uma lista de números inteiros e determine o maior e o menor elemento sem utilizar max() ou min().

import random

lista = []

for i in range(10):
    lista.append(random.randint(1,100))

menor = maior = lista[0]
for i in lista:
    if i < menor:
        menor = i
    if i > maior:
        maior = i

print(f'Na lista {lista}')
print(f'O menor número é: {menor}')
print(f'O maior número é: {maior}')