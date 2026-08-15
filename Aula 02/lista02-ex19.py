# 19. Problema real — Controle de estoque
# Uma pequena loja possui os produtos ["Teclado", "Mouse", "Monitor", "Notebook", "Headset"] e as respectivas quantidades [12, 25, 4, 3, 8].
# Desenvolva um programa que permita consultar um produto, alterar sua quantidade e listar os produtos com estoque inferior a 5 unidades.
# Ao final, informe qual produto possui a maior quantidade em estoque.

import os

produtos = ["Teclado", "Mouse", "Monitor", "Notebook", "Headset"]
quant = [12, 25, 4, 3, 8]
ops = ['Consultar produto',
       'Alterar produto',
       'Listar produtos com estoque baixo',
       'Exibir produto com maior estoque']
estoque_minimo = 0
estoque_maximo = 9999
encerra = False

c_vermelho = "\033[31m"
c_verde = "\033[32m"
c_amarelo = "\033[33m"
c_azul = "\033[34m"
c_clr = "\033[m"

# Valida uma entrada como número e dentro de um limite, quando definido
def validar_op(numero,inicio=0,fim=0):
    try:
        numero = int(numero)
    except:
        print(c_vermelho,'Valor Inválido',c_clr)
        return numero, False
    else:
        if inicio!=0 or fim!=0:
            if numero in range(inicio,fim):
                return numero, True
            else:
                print(c_vermelho,f'Valor fora do limite ({inicio} à {fim-1})!',c_clr)
                return numero, False
        else:
            return numero, True


def consultar_produto(minimo=estoque_minimo, maximo=estoque_maximo):
    print('[xx]','Produto'.ljust(30),'Quantidade'.rjust(15))
    print('='*50)
    for indice,(i,j) in enumerate(zip(produtos,quant)):
        if j in range(minimo,maximo):
            print(f'[{indice:2}] {i:<30}{j:>15}')
    print('='*50)


def alterar_produto():
    esc_valida = False
    while not esc_valida:
        escolha = input('Digite o indice do produto que deseja alterar o estoque: ')
        escolha, esc_valida = validar_op(escolha,0,len(produtos))
    
    esc_valida = False
    while not esc_valida:
        novo_estoque = input(f'Qual o novo estoque do produto {c_amarelo}{produtos[escolha]}{c_clr}: ')
        novo_estoque, esc_valida = validar_op(novo_estoque,0,100000)
    print('='*50)
    quant[escolha] = novo_estoque

    print(f'{c_verde} Estoque atualizado com sucesso: {produtos[escolha]} : {quant[escolha]}{c_clr}')


def menu():
    os.system('cls')
    print('='*50)
    print(f'Exercício 19 - Algoritimos'.center(50))
    print('='*50)
    for k,v in enumerate(ops):
        print(f'[{k+1}] {v}')
    print(f'[0] Sair')
    print('='*50)

    esc_valida = False
    while not esc_valida:
        escolha = input('Escolha uma opção: ')
        escolha, esc_valida = validar_op(escolha,0,len(ops)+1)

    match escolha:
        # Consultar todos os produtos
        case 1:

            os.system('cls')
            consultar_produto(estoque_minimo, estoque_maximo)
        # consultar e alterar estoque
        case 2:
            os.system('cls')
            consultar_produto(estoque_minimo, estoque_maximo)
            alterar_produto()
        # Consultar apenas produtos com estoque < que 5
        case 3:
            os.system('cls')
            consultar_produto(estoque_minimo, 5)

        # Exibir o produto com maior estoque
        case 4:
            os.system('cls')
            consultar_produto(max(quant), estoque_maximo)
        case 0:
            return True
    print()
    input(f'{c_azul}Pressione [Enter] para voltar ao menu inicial.{c_clr}')
    return False
    

while not encerra:
    encerra = menu()

print(c_vermelho,'Programa encerrado...',c_clr)