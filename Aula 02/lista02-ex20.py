# 20. Problema real — Análise de vendas
# Uma empresa registrou as vendas de uma semana na lista vendas = [1250, 980, 1430, 2100, 1750, 890, 1620].
# Desenvolva um programa que calcule o total vendido, a média diária, a maior e a menor venda, quantos dias ficaram acima da média
# e o percentual de dias acima da média.

vendas = [1250, 980, 1430, 2100, 1750, 890, 1620]


soma =0
dias = 0
maior = vendas[0]
menor = vendas[0]
for i in vendas:
    soma += i
    dias += 1
    if i > maior:
        maior = i
    if i < menor:
        menor = i

# soma = sum(vendas)
print(f'Total vendido: {soma}')

media = soma/dias
# media = soma/len(vendas)
print(f'Média diária: {media:.2f}')

# maior = max(vendas)
print(f'Maior venda: {maior}')

# menor = min(vendas)
print(f'Menor venda: {menor}')

dias_acima = 0
for i in vendas:
    if i > media:
        dias_acima += 1
# dias_acima = sum(i > media for i in vendas)
print(f'Dias acima da média: {dias_acima}')

porcentagem = (dias_acima*100)/dias
# porcentagem = (dias_acima*100)/len(vendas)
print(f'Percentual de dias acima da média: {porcentagem:.2f}%')