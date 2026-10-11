# 30. Desafio: Crie um menu com as opções:
# (1) cadastrar valores,
# (2) exibir lista,
# (3) ordenar lista,
# (4) realizar busca sequencial,
# (5) realizar busca binária e
# (0) sair.
# A busca binária só poderá ser realizada quando a lista estiver ordenada.
import os,sys

encerra = False
opc = [
    ['1','Cadastrar valores'],
    ['2','Exibir lista'],
    ['3','Ordenar lista'],
    ['4','Reasizar busca sequencial'],
    ['5','Realizar busca binária'],
    ['0','Sair']
    ]
valores = []

def titulo(txt):
    os.system('cls')
    print('='*50)
    print(f'{txt}'.center(50))
    print('='*50)

def checar_lista(lista):
    return lista == sorted(lista)

def cadastrar_valores(lista):
    repetir = True
    while repetir:

        try:
            valor = int(input('Digite um número para adicionar a lista (-1 para cancelar): '))
        except:
            print('Insira apenas números.')
        else:
            if valor == -1:
                print('Operação cancelada.')
                repetir = False
            elif valor in lista:
                print('O valor já existe na lista.')        
            else:
                lista.append(valor)
                print(f'\033[32m{valor} adicionado a lista, com sucesso.\033[m')
    return lista


def exibir_lista(lista):
    print(f'{lista}'.center(50))


def ordenar_lista(lista):
    lista = sorted(lista)
    print(f'\033[32m Lista ordenada com sucesso. \033[m')
    return lista

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

def gerar_menu():
    print('='*50)
    print('Lista 03 - Exercício 30'.center(50))
    print('='*50)
    for k, v in opc:
        print(f'({k}) {v}')
    print('='*50)

while not encerra:
    os.system('cls')
    gerar_menu()

    opc_valida = False
    while not opc_valida:
        opc_escolha = input('Escolha uma opção: ')
        if opc_escolha in [i[0] for i in opc]:
            opc_valida = True
        else:
            print('Opção inválida.')

    match opc_escolha:
        case '1':
            titulo('Cadastrar Valores')
            valores = cadastrar_valores(valores)

        case '2':
            titulo('Exibir Lista')
            exibir_lista(valores)

        case '3':
            titulo('Ordenar Lista')
            valores = ordenar_lista(valores)

        case '4':
            titulo('Busca Sequencial')
            busca = int(input('Digite um valor a ser buscado na lista: '))
            indice = busca_seq(valores, busca)
            if indice == -1:
                print('O valor não está na lista')
            else:
                print(f'O valor {busca} está na posição {indice} da lista.')

        case '5':
            titulo('Busca Binária')
            if not checar_lista(valores):
                print('\033[31m A lista precisa estar ordenada para realizar a busca binária. \033[m')
            else:
                busca = int(input('Digite um valor a ser buscado na lista: '))
                indice = busca_bin(valores,busca)
                if indice == -1:
                    print('O valor não está na lista')
                else:
                    print(f'O valor {busca} está na posição {indice} da lista.')

        case '0':
            print('Programa encerrado.')
            sys.exit()

    input('\n [Pressione ENTER para voltar ao menu inicial]')
    