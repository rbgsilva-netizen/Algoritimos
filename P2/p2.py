import os

livros = [
    {"ID":103, "Título":"Engenharia de Software"},
    {"ID":101, "Título":"Algoritmos e Lógica de Programação"},
    {"ID":102, "Título":"Banco de Dados"}
    ]

opções = {1: "Cadastrar Livro",
          2: "Listar Livros",
          3: "Ordenar Acervo",
          4: "Buscar Livro",
          0: "Sair",}


def cadastrarLivro():
    print("="*60)
    print("Cadastrar Livro".center(60))
    print("="*60)

    while True:
        try:
            identificação = int(input('ID: '))
            if identificação <=0:
                raise ValueError
        except ValueError:
            print('Entrada inválida')
            continue

        # Verifica se o livro já existe
        existe = False
        for i in livros:
            if i['ID'] == identificação:
                print('Já existe um livro cadastrado com esta ID.')
                existe = True
                break
        if existe:
            continue
        break

    # Verifica se o nome está vazio
    while True:
        titulo = input("Titulo: ").title().strip()
        if not titulo:
            continue
        break

    livro = {}
    livro['ID'] = identificação
    livro['Título'] = titulo
    livros.append(livro)
    print("Livro cadastrado com sucesso!")


def listarLivros():
    print("="*60)
    print("Gerenciador de Acervo de Livros".center(60))
    print("="*60)

    for i in livros:
        print(f'ID: {i['ID']} - {i['Título']}')


def ordenarLivros():
    print("="*60)
    print("Ordenar Acervo".center(60))
    print("="*60)

    while True:
        criterio = input("Defina o critério de ordenação (ID ou Título): ").lower().strip()
        if criterio == "id":
            criterio = "ID"
        elif criterio in ["título","titulo"]:
            criterio = "Título"
        else:
            print('Critério inválido.')
            continue
        break

    n = len(livros)
    for i in range(n-1):
        trocou = False
        for j in range(n-i-1):
            if livros[j][criterio] > livros[j+1][criterio]:
                livros[j], livros[j+1] = livros[j+1], livros[j]
                trocou = True
        if not trocou:
            break

    print(f'Acervo ordenado por {criterio} com sucesso!')


def buscarLivro():
    print("="*60)
    print("Buscar Livro".center(60))
    print("="*60)

    while True:
        try:
            busca = int(input('Buscar ID: '))
            if busca <= 0:
                raise ValueError
        except ValueError:
            print('Entrada Inválida')
        else:
            break

    existe = False
    for i in livros:
        if i['ID'] == busca:
            print(f'ID: [{i["ID"]}] - Título: {i['Título']}')
            existe = True
        
    if not existe:
        print("Livro não encontrado!")
        

# ----------------------------------Principal---------------------------------------------------#
operações = {1: cadastrarLivro,
            2: listarLivros,
            3: ordenarLivros,
            4: buscarLivro}

encerrar = False
while not encerrar:
    os.system("cls")
    print("="*60)
    print("Gerenciador de Acervo de Livros".center(60))
    print("="*60)

    for k, v in opções.items():
        print(f'[{k}] {v}')
    print("-"*60)


    while True:
        try:
            escolha = int(input("Escolha uma opção: "))
            if escolha not in opções:
                raise ValueError
        except ValueError:
            print("Entrada inválida!")
        else:
            break

    if escolha == 0:
        print("Encerrando...")
        encerrar = True
    else:
        os.system("cls")
        operações[escolha]()
        print("-"*60)
        input('[Pressione ENTER para continuar]')
