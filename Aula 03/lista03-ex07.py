# 7. Crie uma lista com números aleatórios.
# Solicite um valor e, usando busca sequencial, informe todas as posições em que esse valor aparece.

import random

lista = [random.randint(1,10) for i in range(10)]
print('Lista:',lista)


busca = int(input('Encontre um valor na lista: '))
encontrado = False

for i in range(len(lista)):
    if lista[i] == busca:
        print(f'O valor {busca} foi encontrado na posição {i}')
        encontrado = True

if not encontrado:
    print(f'O valor {busca} não foi encontrado.')