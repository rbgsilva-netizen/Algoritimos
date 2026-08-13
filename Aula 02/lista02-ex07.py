# 7. Busca de um elemento
# Leia 8 números e armazene-os em uma lista.
# Depois, solicite ao usuário um número para pesquisar.
# Informe se ele está ou não na lista.
# Não utilize index() para realizar a busca.

lista = []
qt_num = 8

# Gerar lista
for i in range(qt_num):
    num = int(input(f'Digite o {i+1}º número: '))
    lista.append(num)

print(f'Numeros digitados: {lista}')

# Buscar na lista
busca = int(input('Digite um número para saber se ele está na lista: '))
if busca in lista:
    print(f'O número {busca} está na lista:')
else:
    print(f'O número {busca} não está na lista:')