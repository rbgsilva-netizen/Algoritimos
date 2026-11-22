# Problema 1 — Controle de notas de uma turma
# Uma instituição de ensino precisa de um programa para registrar as notas de 10 alunos e gerar um resumo do
# desempenho da turma.
# Desenvolva um programa que:
# 1. Armazene em uma lista as notas de 10 alunos.
# 2. Utilize uma função para calcular e retornar a média da turma.
# 3. Utilize outra função para contar quantos alunos foram aprovados (nota maior ou igual a 6).
# 4. Mostre a maior e a menor nota.
# 5. Percorra a lista utilizando uma estrutura iterativa.
# 6. Apresente média, quantidade de aprovados e reprovados.

notas = []

def calcularMedia(notas):
    return sum(notas) / len(notas)


def calcularAprovacao(notas):
    aprovados = 0
    reprovados = 0
    for i in notas:
        if i >= 6:
            aprovados += 1
        else:
            reprovados +=1

    return aprovados, reprovados


for i in range(1, 11):
    notas.append(float(input(f'Insira a nota do {i}º aluno: ')))

media = calcularMedia(notas)
aprovados, reprovados = calcularAprovacao(notas)
maior = max(notas)
menor = min(notas)

print('-'*50)
print(f'Média da turma: {media}')
print(f'Maior nota: {maior}')
print(f'Menor nota: {menor}')
print(f'Aprovados: {aprovados}')
print(f'Reprovados: {reprovados}')
print('-'*50)