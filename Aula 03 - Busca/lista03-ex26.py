# 26. Controle de Estoque: Uma loja possui uma lista de produtos e deseja localizar um produto pelo código.
# Implemente uma solução com busca sequencial e outra com busca binária.
# Compare os resultados.
import random, time


def busca_seq(lista, valor):
    tempo = time.time()
    for k,v in enumerate(lista):
        if v == valor:
            tempo = time.time() - tempo
            return k, tempo
    tempo = time.time() - tempo
    return -1, tempo

def busca_bin(lista,valor):
    pos_ini = 0
    pos_fim = len(lista)-1
    tempo = time.time()
    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2

        if lista[pos_meio] == valor:
            tempo = time.time() - tempo
            return pos_meio, tempo
        elif lista[pos_meio] > valor:
            pos_fim = pos_meio -1
        else:
            pos_ini = pos_meio + 1
    tempo = time.time() - tempo
    return -1, tempo

lista = []
rang_ini = 0
rang_fim = 10000 # 10.000
while len(lista) < 5000: # 5.000
    n = random.randint(rang_ini,rang_fim)
    if n not in lista:
        lista.append(n)
lista = sorted(lista)

# print('Produtos:',lista)
busca = int(input(f'Busque um produto por seu código [{rang_ini} à {rang_fim:,}]: '))


# Busca Sequencial
res_seq, tempo_seq = busca_seq(lista, busca)
print('='*50)
print('Busca Sequencial')
print(f'Tempo de busca: {tempo_seq:.5f} segundos.')
if res_seq == -1:
    print(f'Resultado: Produto não encontrado.')
else:
    print(f'Resultado: Produto encontrado na posição {res_seq}')

# Busca binaria
res_bin, tempo_bin = busca_bin(lista, busca)
print('='*50)
print('Busca Binária')
print(f'Tempo de busca: {tempo_bin:.5f} segundos.')
if res_bin == -1:
    print(f'Resultado: Produto não encontrado.')
else:
    print(f'Resultado: Produto encontrado no indice {res_bin}.')

print('='*50)
print(f'Diferença de tempo: ', end='')
if tempo_seq > tempo_bin:
    print(tempo_seq - tempo_bin)
else:
    print(tempo_bin - tempo_seq)
