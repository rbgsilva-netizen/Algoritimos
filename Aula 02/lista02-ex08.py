# 8. Posição de um elemento
# Considere nomes = ["Ana", "Bruno", "Carlos", "Daniel", "Eduarda"].
# Solicite um nome ao usuário e informe a posição em que ele aparece.
# Caso não exista, informe que o nome não foi encontrado.

nomes = ["Ana", "Bruno", "Carlos", "Daniel", "Eduarda"]


busca = input('Digite um nome para saber se ele está na lista: ').title()

if busca not in nomes:
    print(f'O nome {busca} não foi encontrado!')
else:
    for k, v in enumerate(nomes):
        if busca == v:
            print(f'O nome {busca} está na posição {k} da lista.')
    