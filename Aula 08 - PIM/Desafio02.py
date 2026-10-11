import time

def prova1(a, n):
    return [(i, a**(2*i+1) < 0) for i in range(n+1)]
    

def prova2(a, n):
    return a**(2*n+1) < 0

a = -2
n = 10

temp_ini = time.perf_counter_ns()
p1 = prova1(a,n)
temp_fim = time.perf_counter_ns()
tempo1 = temp_fim - temp_ini

temp_ini = time.perf_counter_ns()
p2 = prova2(a,n)
temp_fim = time.perf_counter_ns()
tempo2 = temp_fim - temp_ini

print(f"""
--- Exercício 04 ---
Para a = {a} e n = {n}:
a) a**(2n+1) < 0: {p2}
Tempo para calcular: {tempo2} nanosegundos.
""")

print("b) Verificando P(n) de 0 até n:")

for k, v in p1:
    print(f"n = {k:<2} | P(n) = {v}")

print(f"Tempo para calcular: {tempo1} nanosegundos.")
