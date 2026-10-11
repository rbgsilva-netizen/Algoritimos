# 29. Agenda Telefônica: Crie uma lista de contatos ordenada alfabeticamente.
# O usuário deve informar um nome e o programa deverá localizá-lo usando busca binária.
# Se encontrado, exiba também o telefone correspondente.


def busca_bin(lista,valor):
    pos_ini = 0
    pos_fim = len(lista)-1
    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2
        if lista[pos_meio] == valor:
            return pos_meio
        elif lista[pos_meio] > valor:
            pos_fim = pos_meio -1
        else:
            pos_ini = pos_meio + 1
    return -1



lista = [
    ["Ana Silva", "Bruno Souza", "Carlos Oliveira", "Daniela Santos", "Eduardo Costa",
     "Fernanda Lima", "Gabriel Alves", "Helena Rocha", "Igor Martins", "João Pereira"],
    
    [21999991001, 21999991002, 21999991003, 21999991004, 21999991005,
     21999991006, 21999991007, 21999991008, 21999991009, 21999991010]
]

busca = input('Buscar nome: ').title()

resultado = busca_bin(lista[0], busca)

if resultado == -1:
    print(f'Nome {busca} não encontrado.')
else:
    print(f'Nome: {busca}')
    print(f'Telefone: {lista[1][resultado]}')