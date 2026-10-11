def calcula_entrega(distancia, peso):
    acrec = 0
    if peso > 5:
        acrec += 2*(peso-5)

    if distancia > 60:
        acrec += 50
    elif distancia > 30:
        acrec += 35
    elif distancia > 10:
        acrec += 20
    else:
        acrec += 12

    return acrec


distancia = float(input(f'Distancia: '))
peso = float(input('Peso: '))

valor_total = calcula_entrega(distancia, peso)

print('-'*50)
print(f'Valor total da entrega: {valor_total}')