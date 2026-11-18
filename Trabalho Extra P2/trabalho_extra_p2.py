import funcoes, random, time, os, sys
from funcoes import ft
0
encerrar = False
lista_desordenada = []
lista_ordenada = []
tempo = {"inicio":0,
         "fim":0,
         "tempo":0}
n = 100000
k = 100000

menu_p = {1: "Gerar lista aleatória",
          2: "Ordenar lista",
          3: "Salvar lista aleatória em lista_desordenada.txt",
          4: "Salvar lista ordenada em lista_ordenada.txt",
          5: "Importar lista de lista_desordenada.txt",
          6: "Alterar o número de elementos da lista",
          0: "Sair",
          "titulo": "Menu Principal"
          }

menu2 = {1: "Selection Sort",
         2: "Bubble Sort",
         3: "Insertion Sort",
         4: "Merge Sort",
         5: "Quick Sort",
         6: "Heap Sort",
         7: "Counting Sort",
         8: "Radix Sort",
         9: "Bucket Sort",
         "titulo": "Métodos De Ordenação"}

algoritmos = {1:funcoes.selectionSort,
        2:funcoes.bubbleSort,
        3:funcoes.insertionSort,
        4:funcoes.mergeSort,
        5:funcoes.quickSort,
        6:funcoes.heapSort,
        7:funcoes.countingSort,
        8:funcoes.radixSort,
        9:funcoes.bucketSort
        }




while not encerrar:
    funcoes.gerarMenu(menu_p)
    print(f"Número de elemntos da lista: {n}")
    if n <=20:
        print(f'Lista desordenada: {lista_desordenada}')
        print(f'Lista ordenada: {lista_ordenada}')
        print("-"*60)
    
    escolha = funcoes.validarEscolha(menu_p)

    match escolha:
        case 1:
            lista_desordenada = [random.randint(1,k) for i in range(n)]
            print(ft("Lista criada com sucesso", 32))
            lista_ordenada = []

        case 2:
            if funcoes.validarLista(lista_desordenada):
                funcoes.gerarMenu(menu2)
                escolha = funcoes.validarEscolha(menu2)

                tempo["inicio"] = time.perf_counter()
                lista_ordenada = algoritmos[escolha](lista_desordenada.copy())
                tempo["fim"] = time.perf_counter()
                tempo["tempo"] = tempo["fim"] - tempo["inicio"]

                print(ft(f"Lista ordenada com sucesso.\nMétodo: {menu2[escolha]}",32))
                print(ft(f"Tempo para ordenar: {tempo["tempo"]*1000000:,.0f} microsegundos",32))

        case 3:
            if funcoes.validarLista(lista_desordenada):
                funcoes.salvarLista(lista_desordenada,ordenada=False)

        case 4:
            if funcoes.validarLista(lista_ordenada):
                funcoes.salvarLista(lista_ordenada,ordenada=True)

        case 5:
            lista_importada = funcoes.importarlista()

            if lista_importada is not None:
                lista_desordenada = lista_importada
                lista_ordenada = []
                n = len(lista_desordenada)

        case 6:
            try:
                novo_n = int(input(f"Digite a quantidade de elementos: "))
                if novo_n <= 0:
                    raise ValueError
                
            except ValueError:
                print(ft("Digite um número inteiro positivo.",31))
            else:
                n = novo_n
                lista_desordenada = []
                lista_ordenada = []
                print(ft(f"Quantidade configurada para {n:,.0f}",32))
        case 0:
            print(ft("Encerrando...",35))
            break
    input(ft("[Pressione ENTER para continuar]",33))
