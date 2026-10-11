# Feito por IA

def anagramas(texto):

    # Caso base
    if len(texto) <= 1:
        return [texto]

    resultado = []

    # Escolhe cada letra para ser a primeira
    for i in range(len(texto)):

        letra = texto[i]

        # Remove a letra escolhida
        restante = texto[:i] + texto[i+1:]

        # Gera recursivamente os anagramas do restante
        anagramas_restante = anagramas(restante)

        # Coloca a letra escolhida na frente de cada anagrama
        for palavra in anagramas_restante:
            resultado.append(letra + palavra)

    return resultado


palavra = "abcd"

resultado = anagramas(palavra)

print(resultado)