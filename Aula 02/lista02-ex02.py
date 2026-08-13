# 2. Percorrendo uma lista
# Considere a lista numeros = [7, 12, 5, 18, 3, 20]. Percorra a lista e exiba cada elemento em uma linha.
# Depois, exiba somente os valores maiores que 10.

numeros = [7,12,5,18,3,20]

for k,v in enumerate(numeros):
    print(f'O {k+1}º elemento da lista é {v}')


maiorQ10 = list(i for i in numeros if i>10)
print(f'Os valores da lista acima de 10 são: ', end='')
print(*maiorQ10)