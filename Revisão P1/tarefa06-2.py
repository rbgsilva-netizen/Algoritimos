# Tarefa 6 - Sistema de Cadastro de Alunos
# Uma escola precisa de um sistema para cadastrar alunos e armazenar suas notas em diferentes disciplinas.
# O sistema deve permitir:
# 1. Adicionar um aluno com seu nome e notas.
# 2. Exibir todos os alunos cadastrados com suas respectivas notas.
# 3. Calcular a média de cada aluno e indicar se ele está aprovado (média ≥ 7) ou reprovado (média < 7).


alunos = []
opcoes = [[1,'Adicionar aluno'],[2,'Exibir Aluno'],[0,'Sair']]

def cadastrar(alunos):
    nome = input('Nome: ').title()
    mat = float(input('Nota de matemática: '))
    por = float(input('Nota de português: '))
    fis = float(input('Nota de Física: '))
    media = (mat + por + fis) / 3
    if media >= 7:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'

    aluno = {'Nome':nome,
             'Matemática':mat,
             'Português': por,
             'Física': fis,
             'Média': media,
             'Situação':situacao
             }
    alunos.append(aluno)

def exibir(alunos):
    if not alunos:
        print('Não há alunos cadastrados')
        return
    
    print('-'*85)
    print(f'{'Nome':<15}{'Matemática':<15}{'Português':<15}{'Física':<15}{'Média':<15}{'Situação':<15}')
    for aluno in alunos:
        print(
            f'{aluno['Nome']:<15}'
            f'{aluno['Matemática']:<15}'
            f'{aluno['Português']:<15}'
            f'{aluno['Física']:<15}'
            f'{aluno['Média']:<15.2f}'
            f'{aluno['Situação']:<15}'
        )
    print('-'*85)


encerrar = False
while not encerrar:
    print('='*60)
    for k, i in opcoes:
        print(f'[{k}] {i}')

    escolha = int(input('Escolha uma opção: '))
    match escolha:
        case 1:
            cadastrar(alunos)
        case 2:
            exibir(alunos)
        case 0:
            encerrar = True