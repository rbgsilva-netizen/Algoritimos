# 2. Escreva uma função recursiva que calcule a potência de um número x elevado a um expoente n.

def potencia(b,e):
    if e == 0:
        return 1
    return b * potencia(b,e-1)

resultado = potencia(2,5)

print(resultado)