# 11. Fatiamento
# Considere valores = [10, 20, 30, 40, 50, 60, 70, 80].
# Utilizando slicing, exiba:
# os quatro primeiros elementos;
# os três últimos;
# os elementos das posições 2 a 5;
# e a lista invertida.


valores = [10, 20, 30, 40, 50, 60, 70, 80]


print(f'Lista: {valores}')
print(f'    Os 4 primeiros elementos da lista são: {valores[:4]}')
print(f'    Os 3 últimos elementos da lista são: {valores[-3:]}')
print(f'    Os elementos de posição 2 a 5 são: {valores[1:5]}')
print(f'    A Lista invertida: {valores[::-1]}')