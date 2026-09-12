# Tarefa 4 - Cálculo Simples de Impostos
# Uma empresa deseja um programa para calcular o valor de impostos sobre um produto, considerando dois tributos:
# 1. ICMS (Imposto sobre Circulação de Mercadorias e Serviços) → 18% sobre o valor do produto.
# 2. ISS (Imposto sobre Serviços) → 5% sobre o valor do serviço.
# O usuário informará o tipo de bem (mercadoria ou serviço) e o valor, e o sistema calculará o imposto devido.


tipo = input('Mercadoria ou Serviço? ').lower()
valor = float(input('Valor: R$ '))
taxa = 0
if tipo == 'mercadoria':
    taxa = 0.18
elif tipo in ['servico','serviço']:
    taxa = 0.05

devido = valor * taxa

print(f'Valor devido: R$ {devido:.2f}')