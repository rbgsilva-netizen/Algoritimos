import funcoes, random, os, time

n = 100000
lista = [random.randint(0,100000) for i in range(n)]
opcoes = [[1,'Selection Sort'],
          [2,'Bubble Sort'],
          [3,'Insertion Sort'],
          [4,'Merge Sort'],
          [5,'Quick Sort'],
          [6,'Heap Sort'],
          [7,'Counting Sort'],
          [8,'Radix Sort'],
          [9,'Bucket Sort'],
          [0,'Sair']]


def menu():
    os.system('cls')

    # Titulo
    print('-'*60)
    print(f'Sort Algorithms ({n:,} elementos)'.center(60))
    print('-'*60)
    for k, v in opcoes:
        print(f'[{k}] {v}')
    print('-'*60)

    #Valida a escolha
    while True:
        try:
            esc = int(input('Escolha uma opção: '))
            if esc not in [k for k, v in opcoes]:
                print('Opção inválida.')
                continue
            break
        except ValueError:
            print('Entrada inválida')

    #Executa escolha
    if esc == 0:
        print('Encerrando...')
        return False

    algoritmos = {
        1:funcoes.selectionSort,
        2:funcoes.bubbleSort,
        3:funcoes.insertionSort,
        4:funcoes.mergeSort,
        5:funcoes.quickSort,
        6:funcoes.heapSort,
        7:funcoes.countingSort,
        8:funcoes.radixSort,
        9:funcoes.bucketSort
        }

    #cria uma copia da lista para não alterar a lista original
    lista2 = lista.copy()

    temp_ini = time.perf_counter()
    lista_ordenada = algoritmos[esc](lista2) #chama a função escolhida
    temp_fim = time.perf_counter()
    temp = temp_fim - temp_ini

    print('-'*60)
    if lista_ordenada == sorted(lista):
        print('Lista ordenada corretamente!')
    else:
        print('Erro na ordenação!')
    # print(f'Lista não-ordenada:{lista}')
    # print(f'Lista ordenada:    {lista_ordenada}')
    print(f'Tempo gasto: {temp:.6f} segundos')
    print(f'Tempo gasto: {temp * 1000000:,.0f} microsegundos')
    print('-'*60)
    input('[Pressione ENTER para limpar a tela e voltar]')



    return True


while menu():
    pass