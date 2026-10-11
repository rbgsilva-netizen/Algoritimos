def calcula_bonificacao(taxa_bonus, salario_base):
    novo_salario = salario_base*(1+(taxa_bonus/100))
    return novo_salario#, bonus

salario_base = float(input('Informe o salario base: '))
taxa_bonus = float(input('Informe a taxa de bonificação: '))

novo_salario = calcula_bonificacao(taxa_bonus,salario_base)
bonus = novo_salario - salario_base

print('-'*50)
print(f'Salário Base: R$ {salario_base:.2f}')
print(f'Salário Atualizado: R$ {novo_salario:.2f}')
print(f'Bonificação consedida: R$ {bonus:.2f}')
print('-'*50)

