import time

def somatorio1(n):
    return sum((i**2) for i in range(1,n+1))

def somatorio2(n):
    return n*(n + 1) * (2*n + 1) // 6

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
--- Desafio 01 ---
Para n = {n} :
a) Soma de i até n onde i² = {soma1} | Tempo para calcular: {tempo1} nanosegundos.
b) 1/6 n(n+1)(2n+1) = {soma2}        | Tempo para calcular: {tempo2} nanosegundos.
''')