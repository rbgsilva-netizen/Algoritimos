# 9. Inserção e remoção
# Crie uma lista inicialmente vazia.
# Leia 5 números e utilize append() para inseri-los.
# Depois, solicite um número ao usuário e remova sua primeira ocorrência, caso exista.
# Exiba a lista antes e depois da remoção.

lista = []
for i in range(5):
    num = int(input(f'Digite o {i+1}º número:'))
    lista.append(num)
print(f'Lista inicial: {lista}')


nova_lista = []
busca = int(input('Escolha um numero para remover sua primeira ocorrência.'))
for i in lista:
    if i != busca:
        nova_lista.append(i)
    else:
        busca = ''
print(f'Lista final: {nova_lista}')