# 3. Escreva uma função recursiva que inverta uma string. Por exemplo, se a entrada for "python", a função deve retornar "nohtyp".

def inverter(texto):
    if len(texto) <= 1:
        return texto
    else:
        return inverter(texto[1:]) + texto[0]

palavra = "ricardo"
resultado = inverter(palavra)
print(resultado)