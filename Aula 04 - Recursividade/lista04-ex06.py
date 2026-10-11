# 6. Escreva uma função recursiva que encontre todos os anagramas de uma string.

def anagramas(texto):
    if len(texto) <= 1:
        return 1
    else:
        return anagramas(texto[:-1]) * len(texto)


palavra = "abcd"
resultado = anagramas(palavra)

print(resultado)