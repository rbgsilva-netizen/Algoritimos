# 3. Soma dos elementos
# Crie uma lista com 8 números inteiros.
# Calcule e exiba a soma de todos os elementos sem utilizar a função sum().

lista = [1,2,3,4,5,6,7,8]
soma = 0
for i in lista:
    soma += i

print(f'A soma dos elementos da lista {lista} é: {soma}')