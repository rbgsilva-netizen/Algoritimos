# Tarefa 6 - Sistema de Cadastro de Alunos
# Uma escola precisa de um sistema para cadastrar alunos e armazenar suas notas em diferentes disciplinas.
# O sistema deve permitir:
# 1. Adicionar um aluno com seu nome e notas.
# 2. Exibir todos os alunos cadastrados com suas respectivas notas.
# 3. Calcular a média de cada aluno e indicar se ele está aprovado (média ≥ 7) ou reprovado (média < 7).

alunos = {'Nome':[],
          'Matemática':[],
          'Português':[],
          'Física':[],
          'Média':[],
          'Situação':[]}

opcoes = ['Sair','Cadastrar Aluno','Exibir Alunos Cadastrados']

def cadastrar(alunos):
    nome = input('Nome: ')
    mat = int(input('Nota em Matematica: '))
    por = int(input('Nota em Português: '))
    fis = int(input('Nota em Física: '))
    media = (mat + por + fis) / 3
    if media >= 7:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'
    alunos['Nome'].append(nome)
    alunos['Matemática'].append(mat)
    alunos['Português'].append(por)
    alunos['Física'].append(fis)
    alunos['Média'].append(media)
    alunos['Situação'].append(situacao)
    return alunos

def exibir(alunos):
    for i in alunos.keys():
        print(f'{i:<10}', end='\t')
    print()
    for v in zip(*alunos.values()):
        for j in v:
            print(f'{j:<10}', end='\t')
        print()

encerra = False
while not encerra:
    print('='*60)
    for k, v in enumerate(opcoes):
        print(f'[{k}] {v}')

    escolha = int(input('Escolha uma opção: '))
    match escolha:
        case 0:
            encerra = True
        case 1:
            alunos = cadastrar(alunos)
        case 2:
            exibir(alunos)