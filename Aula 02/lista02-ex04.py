# 4. Média de uma lista
# Considere notas = [7.5, 8.0, 6.0, 9.5, 5.5].
# Calcule a média manualmente, percorrendo a lista.
# Ao final, informe a média com duas casas decimais.

notas = [7.5, 8.0, 6.0, 9.5, 5.5]

soma = c = 0

for i in notas:
    soma += i
    c += 1
media = soma /c

print(f'A média das notas {notas} é: {media:.2f}')