import time

def mult1(n):
    mult = 1
    for i in range(1,n+1):
        mult *= 1 + (1/i)
    return mult

def mult2(n):
    return n + 1


n = 50

temp_ini = time.perf_counter_ns()
m1 = mult1(n)
temp_fim = time.perf_counter_ns()
tempo1 = temp_fim - temp_ini

temp_ini = time.perf_counter_ns()
m2 = mult2(n)
temp_fim = time.perf_counter_ns()
tempo2 = temp_fim - temp_ini

print(f'''
--- Exercício 04 ---
Para n = {n} :
a) (1 + 1) * (1 + 1/2) * (1 + 1/3) * ... * (1 + 1/n) = {m1:,.0f} | Tempo para calcular: {tempo1} nanosegundos.
b) n + 1 = {m2:,.0f}                                             | Tempo para calcular: {tempo2} nanosegundos.
''')