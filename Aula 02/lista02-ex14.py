# 14. Compreensão de listas
# Considere numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# Crie, utilizando compreensão de listas:
# uma lista com os quadrados;
# uma lista somente com os pares;
# e uma lista contendo apenas os números maiores que 5

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_quad = [i**2 for i in numeros]
lista_par = [i for i in numeros if i%2==0]
lista_maior = [i for i in numeros if i >5]

print(f'Lista com o quadrado dos números: {lista_quad}')
print(f'Lista com os números pares: {lista_par}')
print(f'Lista com valores acima de 5: {lista_maior}')