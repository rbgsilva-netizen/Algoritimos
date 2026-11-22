# Problema 5 — Pontuação em um campeonato
# Em um campeonato, a organização precisa somar a pontuação de uma sequência de participantes e comparar duas
# maneiras de resolver o problema.
# Desenvolva duas soluções:
# 1. Crie uma função iterativa que receba N e calcule a soma de 1 até N utilizando for ou while.
# 2. Crie uma função recursiva que calcule a mesma soma.
# 3. Teste com N = 5, N = 10 e N = 100.
# 4. Apresente os resultados e explique como cada solução funciona.
# 5. Identifique o caso-base e a chamada recursiva.



# Para a soma iterativa, o for percorre uma lista que vai de n até 1, somando cada valor.
def calcularSoma(n):
    soma = 0
    for i in range(n,0,-1):
        soma += i
    return soma


#Para a soma recursiva, a função vai chamando a sí mesma até que chegue ao caso base (1) seja atingindo, então calcula a soma de todos os valores
def calcularSomaRecursiva(n):
    if n == 1:
        return n
    return n+calcularSomaRecursiva(n-1)


n = 5
soma_n = calcularSoma(n)
soma_r = calcularSomaRecursiva(n)
print('-'*30)
print(f'Soma normal: {soma_n}')
print(f'Soma recursiva: {soma_r}')
print('-'*30)
n = 10
soma_n = calcularSoma(n)
soma_r = calcularSomaRecursiva(n)
print(f'Soma normal: {soma_n}')
print(f'Soma recursiva: {soma_r}')
print('-'*30)

n = 100
soma_n = calcularSoma(n)
soma_r = calcularSomaRecursiva(n)
print(f'Soma normal: {soma_n}')
print(f'Soma recursiva: {soma_r}')
print('-'*30)
