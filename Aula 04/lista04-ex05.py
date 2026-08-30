# 5. Escreva uma função recursiva que calcule a soma dos dígitos de um número inteiro positivo.

def soma(x:int):
    if x <= 9:
        return x
    else:
        return soma(x//10) + x % 10


numero = 12345
resultado = soma(numero)

print(resultado)