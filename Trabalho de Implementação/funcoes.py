# Selection Sort (ordenação por seleção)
# Resumo: Encontra o menor elemento da parte não ordenada e o coloca na posição correta, repetindo o processo até ordenar a lista.
# Big O: Melhor O(n²) | Médio O(n²) | Pior O(n²)
# Vantagens: Simples de implementar e realiza poucas trocas de elementos.
# Desvantagens: Possui complexidade O(n²), mesmo em listas já ordenadas.
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
# Resumo: Compara elementos adjacentes e troca suas posições quando estão fora de ordem, fazendo os maiores valores chegarem ao final da lista.
# Big O: Melhor O(n) | Médio O(n²) | Pior O(n²)
# Vantagens: Simples de implementar e eficiente para listas pequenas ou quase ordenadas, quando otimizado.
# Desvantagens: Realiza muitas comparações e trocas, sendo lento para listas grandes.
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
# Resumo: Percorre a lista e insere cada elemento na posição correta dentro da parte já ordenada.
# Big O: Melhor O(n) | Médio O(n²) | Pior O(n²)
# Vantagens: Simples de implementar e eficiente para listas pequenas ou quase ordenadas.
# Desvantagens: Possui complexidade O(n²) em listas grandes e desordenadas.
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
# Resumo: Divide a lista em partes menores até obter elementos individuais e depois intercala essas partes em ordem crescente.
# Big O: Melhor O(n log n) | Médio O(n log n) | Pior O(n log n)
# Vantagens: Desempenho consistente em listas grandes e mantém a estabilidade da ordenação.
# Desvantagens: Exige memória auxiliar e possui implementação mais complexa.
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
# Resumo: Escolhe o último elemento como pivô e reorganiza a lista, colocando os elementos menores ou iguais ao pivô à esquerda e os maiores à direita. Em seguida, aplica o processo recursivamente nas duas partições.
# Big O: Melhor O(n log n) | Médio O(n log n) | Pior O(n²)
# Vantagens: Geralmente apresenta ótimo desempenho na prática e é eficiente para ordenar grandes listas quando as partições são equilibradas.
# Desvantagens: Pode apresentar desempenho O(n²) quando as partições ficam muito desiguais, além de poder atingir o limite de recursão em listas grandes.
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
# Resumo: Organiza os elementos em uma estrutura Max Heap e extrai repetidamente o maior elemento, colocando-o no final da lista.
# Big O: Melhor O(n log n) | Médio O(n log n) | Pior O(n log n)
# Vantagens: Possui desempenho consistente e não exige uma lista auxiliar proporcional ao tamanho da entrada.
# Desvantagens: Implementação mais complexa, não é estável e geralmente apresenta desempenho prático inferior ao Quick Sort.
def heapSort(lista):

    n = len(lista)

    # Constrói o Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    # Extrai os elementos do heap
    for i in range(n - 1, 0, -1):

        lista[0], lista[i] = lista[i], lista[0]

        heapify(lista, i, 0)

    return lista


def heapify(lista, n, i):

    maior = i

    esquerda = 2 * i + 1
    direita = 2 * i + 2

    # Verifica se o filho esquerdo é maior
    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda

    # Verifica se o filho direito é maior
    if direita < n and lista[direita] > lista[maior]:
        maior = direita

    # Se um dos filhos for maior, realiza a troca
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]

        heapify(lista, n, maior)


# Counting Sort (ordenação por contagem)
# Resumo: Conta as ocorrências de cada valor e reconstrói a lista em ordem crescente com base nessas contagens.
# Big O: Melhor O(n + k) | Médio O(n + k) | Pior O(n + k)
# Vantagens: Muito rápido quando os valores pertencem a um intervalo pequeno e conhecido.
# Desvantagens: Exige memória proporcional ao intervalo de valores e funciona apenas com números inteiros.
def countingSort(lista):

    if not lista:
        return lista

    menor = min(lista)
    maior = max(lista)

    # Cria uma lista para armazenar as ocorrências
    contagem = [0] * (maior - menor + 1)

    # Conta as ocorrências de cada elemento
    for num in lista:
        contagem[num - menor] += 1

    # Reconstrói a lista ordenada
    resultado = []

    for i in range(len(contagem)):
        resultado.extend([i + menor] * contagem[i])

    return resultado


# Radix Sort (ordenação por dígitos)
# Resumo: Ordena os números considerando um dígito por vez, começando pelo menos significativo e avançando até o mais significativo.
# Big O: Melhor O(d × n) | Médio O(d × n) | Pior O(d × n)
# Vantagens: Pode ser muito rápido para grandes quantidades de números com quantidade limitada de dígitos.
# Desvantagens: Exige memória auxiliar e depende da quantidade de dígitos dos elementos. Esta implementação aceita apenas inteiros não negativos.
def radixSort(lista):

    if not lista:
        return lista

    maior = max(lista)
    exp = 1

    # Ordena os números de acordo com cada posição decimal
    while maior // exp > 0:

        contagem = [0] * 10
        resultado = [0] * len(lista)

        # Conta as ocorrências dos dígitos
        for num in lista:
            digito = (num // exp) % 10
            contagem[digito] += 1

        # Calcula as posições acumuladas
        for i in range(1, 10):
            contagem[i] += contagem[i - 1]

        # Organiza os elementos de forma estável
        for i in range(len(lista) - 1, -1, -1):
            num = lista[i]
            digito = (num // exp) % 10

            contagem[digito] -= 1
            resultado[contagem[digito]] = num

        lista = resultado
        exp *= 10

    return lista


# Bucket Sort (ordenação por baldes)
# Resumo: Distribui os elementos em diferentes baldes, ordena cada grupo individualmente e depois reúne os elementos em uma única lista.
# Big O: Melhor O(n) | Médio O(n) esperado* | Pior O(n log n)
# Vantagens: Muito eficiente quando os elementos estão distribuídos uniformemente em um intervalo.
# Desvantagens: Depende da distribuição dos dados e pode perder eficiência quando os elementos ficam concentrados em poucos baldes.
def bucketSort(lista):
    if len(lista) <= 1:
        return lista

    menor = min(lista)
    maior = max(lista)

    # Se todos os elementos forem iguais, não gera divisão por 0
    if menor == maior:
        return lista.copy()

    quantidade = len(lista)
    baldes = [[] for _ in range(quantidade)]

    # Distribui os elementos nos baldes
    for num in lista:
        indice = (num - menor) * (quantidade - 1) // (maior - menor)
        baldes[indice].append(num)

    # Ordena individualmente cada balde
    resultado = []

    for balde in baldes:
        balde.sort()
        resultado.extend(balde)

    return resultado
