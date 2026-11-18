import random, os

def ft(txt, cor=37):
    return f"\033[{cor}m{txt}\033[m"


def gerarMenu(menu, cls=True):
    if cls:
        os.system("cls")
    print("="*60)
    print(menu["titulo"].center(60))
    print("="*60)
    for k, v in menu.items():
        if isinstance(k, int):
            print(f"[{k}] {v}")
    print("-"*60)


def validarEscolha(menu):
    opcoes_menu = list(i for i in menu if isinstance(i,int))

    while True:
        try:
            escolha = int(input("Escolha uma opção: "))
        except:
            print(ft("[Erro] Entrada inválida, tente novamente.",31))
        else:
            if escolha in opcoes_menu:
                break
            else:
                print(ft(f"[Erro] Opção disponíveis: {opcoes_menu}", 31))
    return escolha

def validarLista(lista):
    if lista == []:
        print(ft("[Lista vazia. É preciso gerar/importar ou ordenar a lista primeiro]",34))
        return False
    return True

def salvarLista(lista, ordenada=False):
    tipo = "ordenada" if ordenada else "desordenada"

    try:
        with open(f"Trabalho Extra P2/lista_{tipo}.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(str(lista))

    except OSError as erro:
        print(ft(f"[Erro ao salvar arquivo]: {erro}", 31))
    else:
        print(ft(f'Lista salva com sucesso em lista_{tipo}.txt',32))

def importarlista():
    lista = []
    try:
        with open("Trabalho Extra P2/lista_desordenada.txt", "r", encoding="utf-8") as arquivo:
            lista = arquivo.read()
            lista = lista.replace("[","")
            lista = lista.replace("]","")
            lista = lista.replace(","," ")
            lista = lista.split()
            lista = [int(num) for num in lista]
    except ValueError:
        print(ft("O arquivo deve possuir uma lista de números sepados por vírgula.",31))
    except FileNotFoundError:
        print(ft("Arquivo [lista_desordenada.txt] não encontrado.",31))
    except Exception as erro:
            print(ft(f"{type(erro)}: {erro}",31))
    else:
        print(ft("Lista importada com sucesso!",32))
        return lista


# ============================================================================
#                                   Ordenação
# ============================================================================
# Selection Sort (ordenação por seleção)
def selectionSort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if lista[j] < lista[min_index]:
                min_index = j   
        lista[i], lista[min_index] = lista[min_index], lista[i]

    return lista


# Bubble Sort (ordenação por bolha)
def bubbleSort(lista):
    n = len(lista)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                swapped = True
        if not swapped:
            break
    return lista


# Insertion Sort (ordenação por inserção)
def insertionSort(lista):
    n = len(lista)

    for i in range(1, n):
        insert_index = i
        current_value = lista[i]

        for j in range(i-1, -1, -1):
            if lista[j] > current_value:
                lista[j+1] = lista[j]
                insert_index = j
            else:
                break

        lista[insert_index] = current_value

    return lista


# Merge Sort (ordenação por intercalação)
def mergeSort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2

    esquerda = mergeSort(lista[:meio])
    direita = mergeSort(lista[meio:])

    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado


# Quick Sort (ordenação rápida)
def quickSort(lista, inicio=0, fim=None):

    if fim is None:
        fim = len(lista) - 1

    if inicio < fim:

        pivo = particionar(lista, inicio, fim)

        quickSort(lista, inicio, pivo - 1)
        quickSort(lista, pivo + 1, fim)

    return lista


def particionar(lista, inicio, fim):

    pivo = lista[fim]
    i = inicio - 1

    for j in range(inicio, fim):

        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]

    return i + 1


# Heap Sort (ordenação por heap)
def heapSort(lista):

    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    for i in range(n - 1, 0, -1):

        lista[0], lista[i] = lista[i], lista[0]

        heapify(lista, i, 0)

    return lista


def heapify(lista, n, i):

    maior = i

    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda

    if direita < n and lista[direita] > lista[maior]:
        maior = direita

    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]

        heapify(lista, n, maior)


# Counting Sort (ordenação por contagem)
def countingSort(lista):

    if not lista:
        return lista

    menor = min(lista)
    maior = max(lista)

    contagem = [0] * (maior - menor + 1)

    for num in lista:
        contagem[num - menor] += 1

    resultado = []

    for i in range(len(contagem)):
        resultado.extend([i + menor] * contagem[i])

    return resultado


# Radix Sort (ordenação por dígitos)
def radixSort(lista):

    if not lista:
        return lista

    maior = max(lista)
    exp = 1

    # Ordena os números de acordo com cada posição decimal
    while maior // exp > 0:

        contagem = [0] * 10
        resultado = [0] * len(lista)

        for num in lista:
            digito = (num // exp) % 10
            contagem[digito] += 1

        for i in range(1, 10):
            contagem[i] += contagem[i - 1]

        for i in range(len(lista) - 1, -1, -1):
            num = lista[i]
            digito = (num // exp) % 10

            contagem[digito] -= 1
            resultado[contagem[digito]] = num

        lista = resultado
        exp *= 10

    return lista


# Bucket Sort (ordenação por baldes)
def bucketSort(lista):
    if len(lista) <= 1:
        return lista

    menor = min(lista)
    maior = max(lista)

    if menor == maior:
        return lista.copy()

    quantidade = len(lista)
    baldes = [[] for _ in range(quantidade)]

    for num in lista:
        indice = (num - menor) * (quantidade - 1) // (maior - menor)
        baldes[indice].append(num)

    resultado = []

    for balde in baldes:
        balde.sort()
        resultado.extend(balde)

    return resultado
