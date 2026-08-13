# 10. Ordenação
# Considere numeros = [18, 5, 12, 3, 20, 7, 9].
# Exiba a lista original, depois a lista em ordem crescente e finalmente em ordem decrescente.
# Utilize sort() ou sorted() e explique, em comentário no código, a diferença entre eles.

numeros = [18, 5, 12, 3, 20, 7, 9]

print(f'Lista original: {numeros}')
print(f'Lista em ordem crescente: {sorted(numeros)}') # o sorted() organiza os elementos em uma nova lista, sem alterar a original.
numeros.sort(reverse=True) # o sort() organiza a lista original (obs.: o sort() é um metodo de listas)
print(f'Lista em ordem descrecente: {numeros}')