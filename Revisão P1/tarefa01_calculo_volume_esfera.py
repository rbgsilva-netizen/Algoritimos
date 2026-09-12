# Tarefa 1 - Cálculo do Volume de uma Esfera
# Crie um programa em Python que solicite ao usuário o raio de uma esfera e, utilizando funções da biblioteca math, calcule e exiba o volume dessa esfera.

import math

x = float(input('Informe o raio de uma esfera: '))
res = (4/3)*math.pi*x**3

print(res)