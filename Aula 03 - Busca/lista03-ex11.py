# 11. Crie um programa que possua uma lista de CPFs fictícios.
# Solicite um CPF e informe se ele está cadastrado.
# Conte também quantas comparações foram necessárias até encontrá-lo.


def busca_seq(lista, valor):
    comp = 0
    for i in lista:
        comp += 1
        if i == valor:
            return True, comp
    return False, comp

lista = [
    "123.456.789-01",
    "987.654.321-00",
    "111.222.333-44",
    "555.666.777-88",
    "999.888.777-66",
    "234.567.890-12",
    "345.678.901-23",
    "456.789.012-34",
    "567.890.123-45",
    "678.901.234-56"
]

busca = input('Busque um cpf: ')
status, comp = busca_seq(lista, busca)

if status:
    print(f'CPF encontrado após {comp}','comparações.' if comp>1 else 'comparação.')
else:
    print(f'Após {comp} comparações, o CPF informado não foi encontrado.')