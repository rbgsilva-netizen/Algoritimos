# Tarefa 5 - Cálculo deImpostos sobre Salários
# Uma empresa precisa calcular os impostos sobre o salário dos funcionários, considerando três tributos:
#
# 1. INSS
# o 7,5% para salários até R$ 1.500
# o 9% para salários entre R$ 1.500,01 e R$ 3.000
# o 12% para salários acima de R$ 3.000
#
# 2. IRPF (Imposto de Renda Pessoa Física)
# o Isento para salários até R$ 2.000
# o 7,5% para salários entre R$ 2.000,01 e R$ 4.000
# o 15% para salários acima de R$ 4.000
#
# O programa deve calcular o salário líquido após o desconto dos impostos.

bruto = float(input('Salário Bruto: '))

if bruto <= 1500:
    inss = 7.5
elif bruto <= 3000:
    inss = 9
else:
    inss = 12

if bruto <= 2000:
    irpf = 0
elif bruto <= 4000:
    irpf = 7.5
else:
    irpf = 15

inss /= 100
irpf /= 100
liquido = bruto - (bruto*inss) - (bruto*irpf)
print(f'Salário Líquido: R$ {liquido:.2f}')