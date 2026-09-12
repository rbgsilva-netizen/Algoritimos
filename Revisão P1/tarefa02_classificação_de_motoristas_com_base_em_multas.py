# Tarefa 2 - Classificação de Motoristas com Base em Multas
# Uma empresa de transporte deseja classificar seus motoristas com base na quantidade e gravidade das multas recebidas no último ano.
# As categorias são:
# • "Motorista Excelente" → Nenhuma multa registrada.
# • "Motorista Bom" → No máximo 2 multas leves.
# • "Motorista Regular" → Até 4 multas leves ou 1 multa grave.
# • "Motorista Ruim" → Mais de 4 multas leves ou até 2 multas graves.
# • "Motorista Perigoso" → Mais de 2 multas graves ou qualquer multa gravíssima.
#
# O sistema deve receber a quantidade de multas leves, graves e gravíssimas e classificar o
# motorista




mleve = int(input('Insira a quantidade de Multas Leves: '))
mgrave = int(input('Insira a quantidade de Multas Graves: '))
mgravissima = int(input('Insira a quantidade de Multas Gravíssimas: '))


if mgrave > 2 or mgravissima > 0:
    print('Motorista Perigoso')

elif mleve > 4 or (1 < mgrave <= 2):
    print('Motorista Ruim')

elif (2 < mleve <= 4) or mgrave == 1:
    print('Motorista Regular')

elif (0 < mleve <= 2) and mgrave == 0 and mgravissima == 0:
    print('Motorista Bom')

else:
    print('Motorista Excelente')