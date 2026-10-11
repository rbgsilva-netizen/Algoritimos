def calcular_media(lista):
    return sum(lista)/len(lista)


nome = input('Nome do aluno: ')
notas = []
for i in range(1,9):
    nota = float(input(f'Insira a {i}º nota: '))
    notas.append(nota)

media = calcular_media(notas)
if media >= 8:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

print(f'Aluno: {nome}')
print(f'Média: {media:.2f}')
print(f'Situação: {situacao}')