# 6. Dada uma lista de números inteiros, utilize busca sequencial para localizar o maior valor sem utilizar as funções max() ou sort().
import random

lista = []
while len(lista) < 10:
    n = random.randint(1,100)
    if n not in lista:
        lista.append(n)

print(lista)

maior1 = lista[0]

for i in lista[1:]:
    if i > maior1:
        maior1 = i

print(f'Maior número: {maior1}')
