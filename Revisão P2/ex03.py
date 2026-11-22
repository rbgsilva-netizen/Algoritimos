# Problema 3 — Sistema de pedidos de uma lanchonete
# Uma lanchonete deseja controlar os valores dos pedidos realizados durante um dia. Os valores devem ser
# armazenados até que o usuário encerre o cadastro.
# Desenvolva um programa que:
# 1. Registre os valores dos pedidos em uma lista; a entrada termina quando o usuário digitar 0.
# 2. Crie uma função para calcular o faturamento total.
# 3. Crie uma função para identificar o maior pedido.
# 4. Crie uma função para calcular a média dos pedidos.
# 5. Utilize while para controlar a entrada.
# 6. Exiba quantidade de pedidos, faturamento, maior pedido e média.

pedidos = []


def calcularFaturamento(lista):
    return sum(lista)

def maiorPedido(lista):
    maior = 0
    for i in lista:
        if i > maior:
            maior = i
    return maior

def calcularMedia(lista):
    return sum(lista) / len(lista)



encerrar = False
while not encerrar:
    entrada = float(input('Registre o valor do pedido [digite 0 para encerrar]: '))
    if entrada == 0:
        encerrar = True
    else:
        pedidos.append(entrada)

faturamento = calcularFaturamento(pedidos)
maior_pedido = maiorPedido(pedidos)
media_pedidos = calcularMedia(pedidos)


print('-'*60)
print(f'Quantidade de pedidos: {len(pedidos)}')
print(f'Faturamento total: R$ {faturamento:.2f}')
print(f'Maior pedido: R$ {maior_pedido:.2f}')
print(f'Média dos pedidos: R$ {media_pedidos:.2f}')
print('-'*60)