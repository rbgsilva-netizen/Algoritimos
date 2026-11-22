def somaRecursiva(lista:list):
    if lista == []:
        return 0
    
    return lista[0] + somaRecursiva(lista[1:])


lista = [1,2,3,4,5]
soma = somaRecursiva(lista.copy())
print(soma)