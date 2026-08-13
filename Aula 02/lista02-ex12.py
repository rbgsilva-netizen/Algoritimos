# 12. Lista sem repetição
# Dada a lista numeros = [2, 5, 2, 8, 5, 9, 2, 8, 10], crie uma nova lista contendo cada valor apenas uma vez, mantendo a ordem da primeira ocorrência.
# Não utilize set().

numeros = [2, 5, 2, 8, 5, 9, 2, 8, 10]
nova_lista = []

for i in numeros:
    if i not in nova_lista:
        nova_lista.append(i)


print(f'Lista original: {numeros}')
print(f'Nova lista: {nova_lista}')