# 16. Lista de listas
# Crie uma matriz 3x3 utilizando listas de listas.
# Exiba todos os elementos, a soma de todos os valores e a soma de cada linha.

lista = [[1,2,3], [4,5,6], [7,8,9]]
somal = 0
somaf = 0

for i in lista:
    for j in i:
        print(j,end=' ')
        somal += j
    print(f'\t\tsoma da linha: {somal}')
    somaf += somal
    somal = 0

print(f'\t\tSoma de todos os elementos: {somaf}')