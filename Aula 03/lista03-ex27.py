# 27. Cadastro de Alunos: Dada uma lista de matrículas, crie um programa que permita ao usuário escolher entre busca sequencial ou busca binária.
# Para a busca binária, garanta que a lista esteja ordenada.
import random

def busca_seq(lista, valor):
    for k,v in enumerate(lista):
        if v == valor:
            return k
    return -1

def busca_bin(lista,valor):
    pos_ini = 0
    pos_fim = len(lista)-1
    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2
        if lista[pos_meio] == valor:
            return pos_meio
        elif lista[pos_meio] > valor:
            pos_fim = pos_meio -1
        else:
            pos_ini = pos_meio + 1
    return -1

lista = []
alfa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'
for i in range(10):
    elemento = ''
    for _ in range(2):
        elemento += random.choice(alfa)
    elemento += '-'
    for _ in range(4):
        elemento += random.choice(nums)
    lista.append(elemento)
lista = sorted(lista)
print(f'Matriculas: {lista}')

busca = input('Digite a matricula: ').upper()
op = input('Digite 0 para Busca Sequencial ou 1 para Busca Binária: ')[0]
resultado = -1
print('='*50)
match op:
    case '0':
        resultado = busca_seq(lista, busca)
        print('Busca Sequencial:')
    case '1':
        print('Busca Binária:')
        resultado = busca_bin(lista, busca)
    case _:
        print('Opção inválida')

if resultado != -1:
    print(f'Valor encontrado na posição {resultado}')
else:
    print('Valor não encontrado ou opção iválida')