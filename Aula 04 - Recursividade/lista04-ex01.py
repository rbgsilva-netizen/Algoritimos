# 1. Escreva uma função recursiva que calcule o máximo divisor comum (MDC) de dois números inteiros a e b.

def mdc(a,b):

    if a % b == 0:
        return b
    else:
        return mdc(b, a % b)



a = 12
b = 18
resultado = mdc(a,b)
print(resultado)