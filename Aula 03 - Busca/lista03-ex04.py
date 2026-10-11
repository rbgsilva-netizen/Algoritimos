# 4. Dada uma lista de notas de alunos, solicite uma nota e verifique, por meio da busca sequencial, se ela aparece na lista.
# Informe também quantas vezes ela ocorre.
import random

notas = [round(random.uniform(1,10),1) for i in range(10)]
print(f'Lista de notas: {notas}')
nota = float(input("Busque uma nota na lista de [0 à 10]: "))

c = 0
for i in notas:
    if i == nota:
        c += 1

print(f'A nota {nota}', f'tem {c} ocorrências na lista.' if c > 0 else 'não tem ocorrências na lista.')