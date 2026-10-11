# 1. Crie uma lista com 10 números inteiros e desenvolva um programa que solicite ao usuário um número.
# Utilize a busca sequencial para informar se o número está presente na lista.

import random


def busca_seq(lista, numero):
    n = len(lista)
    for i in range(n):
        if lista[i] == numero:
            return f"O número {numero} está na posição {i} da lista."
    return f"O número {numero} não está na lista"


lista = list(random.randint(1,20) for i in range(10))
print(lista)

numero = int(input('Digite um número inteiro: '))
busca = busca_seq(lista,numero)
print(busca)