import os

obras = {"Título":["Livro1"],
         "Data de criação":["05/06/1980"],
         "Tema":["Tema1"],
         "Estilo artístico":["Estilo1"],
         "Descrição":["Descrição1"],
         "Técnica utilizada":["Técnica1"],
         "Autor":["Autor1"],
         "Localização":["Localização1"],
         "Documentos":["Documento1"]
         }

artistas = {"Nome":[],
            "Data de nascimento":[],
            "Local de nascimento":[],
            "biografia":[],
            "Estilos artísticos":[]
            }

estilos = {"Denominação":[],
           "Período de influência":[],
           "Características predominantes":[],
           "Escola representativa":[]
           }

empréstimos = {"Período":[],
               "Nome do evento":[],
               "Responsável":[],
               "Tema":[]
               }


visita = {"Tema":[],
          "Descrição":[],
          "Obras":[],
          }


opcoes = {1:"Cadastrar Obra",
          2:"Cadastrar Artista",
          3:"Cadastrar Estilo",
          4:"Buscar Obra",
          5:"Buscar Artista",
          6:"Buscar Estilo",
          7:"Realizar emprestimo",
          8:"Agendar Visita Guiada",
          0:"Sair"}


def cadastrarObra():
    os.system("cls")
    print("="*60)
    print("Cadastro de Obras".center(60))
    print("="*60)

    obras["Título"].append(input("Titulo: "))
    obras["Data de criação"].append(input("Data de criação: "))
    obras["Tema"].append(input("Tema: "))
    obras["Estilo artístico"].append(input("Estilo artístico: "))
    obras["Descrição"].append(input("Descrição: "))
    obras["Técnica utilizada"].append(input("Técnica utilizada: "))
    obras["Autor"].append(input("Autor: "))
    obras["Localização"].append(input("Localização: "))
    obras["Documentos"].append(input("Documento: "))

def buscarObra(dicionario):
    os.system("cls")
    print("="*60)
    print("Buscar Obra".center(60))
    print("="*60)

    print("Opções:")
    for i in dicionario["Título"]:
        print(i)
    print('-'*60)

    while True:
        escolha = input("Insira o título da obra que deseja pesquisar: ").title()
        if escolha in dicionario["Título"]:
            for k, v in dicionario.items():
                print(f"{k}: {v}")
            break
        else:
            print("Título não encontrado.")


encerrar = False
while not encerrar:
    os.system("cls")
    print("="*60)
    print("Museu de Artes".center(60))
    print("="*60)
    for k, v in opcoes.items():
        print(f'[{k}] - {v}')
    print("="*60)
    
    while True:
        try:
            escolha = int(input('Escolha uma opção: '))
        except:
            print("Entrada inválida!")
        else:
            if escolha not in opcoes.keys():
                print("Opção inválida")
            else:
                break
    
    match escolha:
        case 1:
            cadastrarObra()
            print('Obra cadastrada com sucesso!')
            print(obras)

            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            buscarObra(obras)
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            pass
        case 0:
            print("Encerrando...")
            encerrar = True

    input("[Pressione ENTER para continuar]")
