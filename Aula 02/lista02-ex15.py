# 15. Listas paralelas
# Crie duas listas: uma com 5 nomes de alunos e outra com suas respectivas notas.
# Percorra as listas simultaneamente e exiba o nome, a nota e a situação de cada aluno, considerando aprovação com nota maior ou igual a 6.

nomes = ['Ricardo','João','Ana','Maria','José']
notas = [8,7.5,5.3,6,6.3]

print(f'{'Nome':<20} Notas \t\t Situação')
for i in range(len(nomes)):
    situacao = "Aprovado" if notas[i] >= 6 else "Reprovado"
    print(f'{nomes[i]:<20}  {notas[i]:.1f} \t\t {situacao}')