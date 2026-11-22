# Uma empresa está avaliando dois trechos de código para processar registros de clientes. O objetivo é entender
# como o número de operações cresce conforme aumenta a quantidade de registros.

# Algoritmo A
# for i in range(n):
#     print(i)

# Algoritmo B
# for i in range(n):
#     for j in range(n):
#         print(i, j)


# Responda:
# 1. Quantas vezes print será executado no Algoritmo A para N = 5?
# Resposta: o print será executado 5 vezes

# 2. Quantas vezes será executado no Algoritmo B para N = 5?
# Resposta: o print será executado 25 vezes (n²)

# 3. Determine a complexidade de tempo de cada algoritmo usando Big O.
# Resposta: Algoritmo A = O(n). Algoritmo B = O(n²)

# 4. Explique por que o Algoritmo B tende a exigir mais operações quando N aumenta.
# Resposta: Porque o algoritmo possui dois laços aninhados, fazendo com que o segundo laço percorra todos os elementos para cada iteração do primeiro laço.
# Dessa forma o número de operações cresce proporcionalmente ao quadrado de N.

# 5. Compare o impacto de aumentar N de 5 para 100.
# Resposta: Para o Algoritmo A, aumentaria o numero de iterações de 5 para 100.
#           Para o Algoritmo B, aumentaria o número de iterações de 25 para 10.000