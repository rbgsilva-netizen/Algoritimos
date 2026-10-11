# 8. Desenvolva uma função que receba uma lista e um número e retorne True se o número existir na lista e False caso contrário.
# A função deve utilizar busca sequencial.

def busca_sequencial(lista,numero):
    for i in lista:
        if i == numero:
            return True
    return False

lista = [1,5,6,8,7]
n = 9

if busca_sequencial(lista,n):
    print('achou')
else:
    print('não achou')