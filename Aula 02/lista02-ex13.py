# 13. Valores acima da média
# Leia 10 números reais e armazene-os em uma lista.
# Calcule a média e depois exiba somente os valores que ficaram acima da média.

lista = []
c = 10
for i in range(c):
    n = float(input(f'Digite o {i+1}º número real: '))
    lista.append(n)
print(f'Lista de números Digitados: {lista}')

soma = 0
for i in lista:
    soma += i
media = soma/c
print(f'A média é: {media}')


nova_lista = list(i for i in lista if i > media)
print(f'Os valores acima da média são: {nova_lista}')