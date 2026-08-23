# 16. Crie uma lista ordenada com 20 números.
# Realize uma busca binária e exiba, a cada iteração, os valores das variáveis inicio, fim e meio.
import random

def busca_binaria(lista, valor):
    posIni = 0
    posFim = len(lista) - 1
    while posIni <= posFim:
        posMeio = (posIni + posFim) // 2
        print('-'*20)
        print(f'Posição inicial: {posIni} (valor:{lista[posIni]})')
        print(f'Posição do meio: {posMeio} (valor:{lista[posMeio]})')
        print(f'Posição final: {posFim} (valor:{lista[posFim]})')

        if lista[posMeio] == valor:
            return posMeio
        elif lista[posMeio] > valor:
            posFim = posMeio - 1
        else:
            posIni = posMeio + 1
    return -1

lista = []
while len(lista) < 20:
    n = random.randint(0,100)
    if n not in lista:
        lista.append(n)
lista = sorted(lista)

resultado = busca_binaria(lista,10)

print('='*92)
print(f'Lista gerada: {lista}')
if resultado == -1:
    print('Busca pelo número 10: Não encontrado.')
else:
    print(f'Busca pelo número 10: Encontrado na posição {resultado}.')