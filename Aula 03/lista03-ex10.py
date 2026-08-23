# 10. Dada uma lista de palavras, utilize busca sequencial para encontrar a palavra com maior quantidade de caracteres.
# Não utilize max() com chave.

lista = ["Rio de Janeiro","São Paulo","Parana","Minas Gerais","Santa Catarina","Saquarema"]
maior_palavra = lista[0]

for i in lista:
    if len(i) > len(maior_palavra):
        maior_palavra = i

print(f'Lista de palavras: {lista}')
print(f'Maior palavra na lista: {maior_palavra}')