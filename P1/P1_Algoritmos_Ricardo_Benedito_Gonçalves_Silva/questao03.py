def calcula_import_de_renda(salario):
    deducao = 0
    if salario > 4664.68:
        deducao = 908.73
        taxa = 27.5
    elif salario >= 3751.06:
        deducao = 675.49
        taxa = 22.5
    elif salario >= 2826.66:
        deducao = 394.16
        taxa = 15
    elif salario >= 2428.81:
        deducao = 182.16
        taxa = 7.5
    else:
        deducao = 0
        taxa = 0

    return salario*(taxa/100) + deducao


salario = float(input('Salário bruto: '))
devido = calcula_import_de_renda(salario)

print(f'Para o salário R$ {salario} o imposto devido é R$ {devido:.2f}')