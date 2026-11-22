# Problema 4 — Consulta de estoque
# Um comércio mantém uma lista com as quantidades disponíveis de determinado produto em cada uma de suas 6
# unidades. O responsável deseja consultar o estoque total e identificar unidades sem produtos.
# Desenvolva um programa que:
# 1. Armazene em uma lista as quantidades em estoque das 6 unidades.
# 2. Crie uma função que retorne a soma total dos itens.
# 3. Crie uma função que conte quantas unidades estão com estoque igual a zero.
# 4. Crie uma função que receba uma quantidade desejada e informe se alguma unidade possui exatamente essa
# quantidade.
# 5. Utilize laços de repetição para percorrer os dados.

lista = [5,8,9,7,0,3]

def calcularSoma(lista):
    return sum(lista)


def calculaZero(lista):
    unidades = 0
    for i in lista:
        if i == 0:
            unidades += 1

    return unidades


def encontrarQtd(k, lista):
    n = len(lista)

    for i in range(n):
        if lista[i] == k:
            return i

    return -1

soma = calcularSoma(lista)
zerado = calculaZero(lista)

busca = int(input('Digite a quantidade que deseja buscar: '))
resultado = encontrarQtd(busca, lista)


print(f'Soma de todas as unidades: {soma}')
print(f'Unidades com zero estoque: {zerado}')

if resultado == -1:
    print(f'Nenhuma unidade possui exatamente {busca}.')
else:
    print(f'A unidade {resultado} possui exatamente {busca}.')