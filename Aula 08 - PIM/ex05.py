import time

def divide1(n):
    return [(i, (i**2 + i) % 2 == 0) for i in range(1,n+1)]


def divide2(n):
    return ((n**2) + n) % 2 == 0


n = 7

temp_ini = time.perf_counter_ns()
div1 = divide1(n)
temp_fim = time.perf_counter_ns()
tempo1 = temp_fim - temp_ini

temp_ini = time.perf_counter_ns()
div2 = divide2(n)
temp_fim = time.perf_counter_ns()
tempo2 = temp_fim - temp_ini

print(f'''
--- Exercício 05 ---
Para n = {n} : 
a) 2 divide n² + n = {div2} | Tempo para calcular: {tempo2} nanosegundos.
''')

print(f'b) De i até n, verificando se 2 divide n² + n')
for k, v in div1:
    print(f'Valor: {k} = {v}')
print(f'Tempo para calcular: {tempo1} nanosegundos.')