import time

def somatorio1(n):
    return sum((3*i-1) for i in range(1,n+1))
    
    

def somatorio2(n):
    return (n*(1+(3*n))) / 2


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
--- Exercício 03 ---
Para n = {n} :
a) 2 + 5 + 8 + ... + (3n-1) = {soma1:,.0f} | Tempo para calcular: {tempo1} nanosegundos.
b) ( n(1+3n) )/2 = {soma2:,.0f}            | Tempo para calcular: {tempo2} nanosegundos.
''')