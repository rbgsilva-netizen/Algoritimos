import os

dados = {"obras":[],
         "artitas":[],
         "estilos":[],
         "emprestimos":[],
         "visitas":[]
         }


opções = {1:"Cadastrar Obra",
          2:"Cadastrar Artista",
          3:"Cadastrar Estilo",
          4:"Buscar Obra",
          5:"Buscar Artista",
          6:"Buscar Estilo",
          7:"Realizar emprestimo",
          8:"Agendar Visita Guiada",
          0:"Sair"
          }


def cadastrar():
    os.system("cls")
    print("="*60)
    print("Cadastrar".center(60))
    print("="*60)

    print("Escolha uma opção abaixo ('sair' para voltar ao menu inicial):")
    for i in dados:
        print(f"> {i}")
    while True:
        escolha = input("\n >> ")
        if escolha == 'sair':
            return
        elif escolha not in dados:
            print("Opção inválida!")
        else:
            break

def bubbleSort():
    titulos = obras["Título"]

    n = len(titulos)

    for i in range(n-1):
        trocou = False
        for j in range(n-i-1):
            if titulos[j] > titulos[j+1]:
                for lista in obras.values():
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
        if not trocou:
            break
    
    
obras = {"Título":["Livro1","Livro0"],
         "Data de criação":["05/06/1980", "05/07/2000"],
         "Tema":["Tema1", "tema0"],
         "Estilo artístico":["Estilo1", "Estilo0"],
         "Descrição":["Descrição1","Descrição0"],
         "Técnica utilizada":["Técnica1", "técnica0"],
         "Autor":["Autor1", "Autor0"],
         "Localização":["Localização1", "localização0"],
         "Documentos":["Documento1", "documento0"]
         }

for k, v in obras.items():
    print(f'{k} - {v}')
bubbleSort()
print()
for k, v in obras.items():
    print(f'{k} - {v}')