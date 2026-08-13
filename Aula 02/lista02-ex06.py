# 6. Contagem de pares e ímpares
# Dada uma lista com 10 números inteiros, conte quantos são pares e quantos são ímpares.
# Exiba as duas quantidades ao final.

import random

lista =[]
par = []
impar = []

for i in range(10):
    num = random.randint(1,100)
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f'Na lista {lista}:')
print(f'Os numeros pares desta lista são: {par}')
print(f'Os numeros impares desta lista são: {impar}')




