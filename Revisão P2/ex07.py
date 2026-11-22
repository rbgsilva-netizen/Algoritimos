# Problema 7 — Desafio integrador: ranking de participantes
# Uma organização realizará uma competição e precisa registrar pontuações, calcular estatísticas e gerar um ranking
# em ordem decrescente.
# Requisitos do programa:
# 1. Armazene pontuações em uma lista. O cadastro termina quando o usuário digitar -1.
# 2. Crie uma função para calcular a média.
# 3. Crie uma função para identificar a maior pontuação.
# 4. Implemente Bubble Sort para ordenar em ordem decrescente.
# 5. Crie uma função recursiva para somar as pontuações, considerando uma lista vazia como caso-base.
# 6. Utilize uma estrutura iterativa para exibir o ranking numerado.
# 7. Apresente quantidade de participantes, média, maior pontuação e ranking.


pontuacoes = []

def calcularMedia(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)


def maiorPonto(lista):
    if not lista:
        return 0
    return max(lista)


def bubbleSort(lista):
    n = len(lista)
    for i in range(n-1):
        trocou = False
        for j in range(n-i-1):
            if lista[j] < lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
        if not trocou:
            break

    return lista


def somaRecursiva(lista):
    if lista == []:
        return 0

    return lista[0] + somaRecursiva(lista[1:])


while True:
    pontuacao = float(input("Digite a pontuação: "))
    if pontuacao != -1:
        pontuacoes.append(pontuacao)
        continue
    break

media = calcularMedia(pontuacoes)
maior = maiorPonto(pontuacoes)
soma = somaRecursiva(pontuacoes)
pontuacoes_d = bubbleSort(pontuacoes.copy())

print('-'*50)
print('Ranking (Decrescente):')
for k, v in enumerate(pontuacoes_d):
    print(f'{k+1}º colocado - {v}')

print(f'Quantidade de participantes: {len(pontuacoes)}')
print(f'Soma das pontuações: {soma}')
print(f'Média das pontuações: {media}')
print(f'Maior pontuação: {maior}')
print('-'*50)