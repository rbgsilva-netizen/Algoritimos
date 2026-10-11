# 4. Escreva uma função recursiva que verifique se uma string é um palíndromo.
# Um palíndromo é uma palavra ou frase que se lê da mesma forma de trás para frente, ignorando espaços, maiúsculas e minúsculas.
# Por exemplo, "arara" é um palíndromo.

def palindromo(texto):
    texto = texto.replace(" ","").lower()

    if len(texto) <= 1:
        return True
    if texto[0] != texto[-1]:
        return False
    return palindromo(texto[1:-1])

palavra = "A Ra rA"
resultado = palindromo(palavra)

if resultado:
    print(f'{palavra} é um palíndromo.')
else:
    print(f'{palavra} não é um palíndromo.')