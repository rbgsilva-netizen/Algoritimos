# 9. Uma escola possui uma lista com os números de matrícula dos alunos.
# Solicite uma matrícula e verifique se o aluno está cadastrado utilizando busca sequencial.

def busca_seq(lista,valor):
    for i in lista:
        if i == valor:
            return True
    return False

matriculas = [1678,7896,1358,6428,3912]
print(f'Matriculas cadastradas: {matriculas}')
n = int(input('Busque um aluno por sua matricula: '))

if busca_seq(matriculas, n):
    print(f'O aluno com matricula {n} está cadastrado!')
else:
    print(f'Não há registro da matricula {n}')