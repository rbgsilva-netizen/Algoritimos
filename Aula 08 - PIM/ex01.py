import time

def somatorio_1(n):
    return sum((2**(i-1)) for i in range(1,n+1))
    # soma = 0
    # for i in range(1,n+1):
    #     soma += 2**(i-1)
    # return soma
    
def somatorio_2(n):
    return 2**n-1


n = 10

temp_ini = time.perf_counter_ns()
soma1 = somatorio_1(n)
temp_fim = time.perf_counter_ns()
tempo1 = temp_fim - temp_ini

temp_ini = time.perf_counter_ns()
soma2 = somatorio_2(n)
temp_fim = time.perf_counter_ns()
tempo2 = temp_fim - temp_ini

print(f'''
--- Exercício 01 ---
Para n = {n} :
a) 1 + 2 + 4 + ... + n^(n-1) = {soma1:,.0f} | Tempo para calcular: {tempo1} nanosegundos.
b) n^n - 1 = {soma2:,.0f}                   | Tempo para calcular: {tempo2} nanosegundos.
''')
