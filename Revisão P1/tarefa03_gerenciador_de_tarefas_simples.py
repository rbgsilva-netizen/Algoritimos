# Tarefa 3 - Gerenciador de Tarefas Simples
# Uma pessoa deseja um programa para gerenciar suas tarefas diárias. O sistema deve permitir:
# • Adicionar uma nova tarefa à lista de tarefas pendentes.
# • Listar todas as tarefas pendentes.
# • Marcar uma tarefa como concluída, removendo-a da lista.


tarefas = []
opcoes = ['Inserir Tarefa','Listar Tarefas','Marcar Tarefa como concluída', 'Sair']

def inserirTarefa(nova_tarefa):
    tarefas.append(nova_tarefa)
    return tarefas
    

def listarTarefas(tarefas):
    if tarefas == []:
        print('Não há tarefas')
        return False
    else:
        for k, v in enumerate(tarefas):
            print(f'({k}) {v}')
        return True


def concluirTarefa(tarefas):
    excluir = int(input('Digite o indice da tarefa que deseja excluir: '))
    tarefas.pop(excluir)

    return tarefas


encerrar = False
while not encerrar:
    print('='*60)
    for k, v in enumerate(opcoes):
        print(f'[{k}] {v}')

    escolha = int(input('Escolha uma opção: '))
    match escolha:
        case 0:
            nova_tarefa = input('Tarefa a ser incluída: ')
            tarefas = inserirTarefa(nova_tarefa)
        case 1:
            listarTarefas(tarefas)
        case 2:
            haTarefa = listarTarefas(tarefas)
            if haTarefa:
                tarefas = concluirTarefa(tarefas)
        case 3:
            encerrar = True
