# 5. Crie uma lista de produtos e uma lista correspondente de preços.
# Solicite o nome de um produto e utilize busca sequencial para localizar o produto e exibir seu preço.

def buscar_preco(produtos,precos, valor):
    for i in range(len(produtos)):
        if produtos[i].lower() == valor.lower():
            return f'O {valor} custa R${precos[i]:.2f}'
        
    return f'O produto {valor} não foi encontrado.'

produtos = [
    "Teclado",
    "Mouse",
    "Monitor",
    "Headset",
    "Webcam",
    "SSD 480GB",
    "Memória RAM 8GB",
    "Mousepad",
    "Notebook",
    "Caixa de Som"
]

precos = [
    120.00,
    75.50,
    899.90,
    199.99,
    150.00,
    280.00,
    220.50,
    45.90,
    3500.00,
    180.00
]
        

print(produtos)
busca = input("Digite o nome do produto para saber seu valor: ")

resultado = buscar_preco(produtos,precos,busca)
print(resultado)
