import time

def somatorio1(n):
    return sum(i*(i+1) for i in range (1,n+1))
    # soma = 0
    # for i in range(1,n+1):
    #     soma += i*(i+1)
    # return soma

def somatorio2(n):
    return (n*(n+1)*(n+2))/3


n = 10

temp_ini = time.perf_counter_ns()
soma1 = somatorio1(n)
temp_fim = time.perf_counter_ns()
tempo1 = temp_fim - temp_ini

temp_ini = time.perf_counter_ns()
soma2 = somatorio2(n)
temp_fim = time.perf_counter_ns()
tempo2 = temp_fim - temp_ini

print(f'''
--- Exercício 02 ---
Para n = {n} :
a) Soma de i até n para i(i+1) = {soma1:,.0f} | Tempo para calcular: {tempo1} nanosegundos.
b) (n*(n+1)*(n+2)) / 3 = {soma2:,.0f}         | Tempo para calcular: {tempo2} nanosegundos.
''')