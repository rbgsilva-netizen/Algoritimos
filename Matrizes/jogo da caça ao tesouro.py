import random
import os


matriz = [["?" for j in range(5)] for i in range(5) ]
linha_random = random.randint(0,4)
coluna_random = random.randint(0,4)
tentativas = 0
status = ""


def gerarmatriz():
    os.system('cls')
    global tentativas
    titulo = "Caça ao tesouro"
    print(f"{titulo.center(22)}")
    print('='*22)
    print('\033[33m    1   2   3   4   5\033[m')
    for k, v in enumerate(matriz):
        print()
        print(f'\033[33m{k+1}\033[m', end='')
        for j in v:
            if j == "X":
                print(f'\033[31m{j:>4}\033[m',end='')
            elif j == "T":
                print(f'\033[32m{j:>4}\033[m',end='')
            else:
                print(f'\033[34m{j:>4}\033[m',end='')
        print()
    print('='*22)
    print(f'Tentativas: {tentativas}')
    print(f'Status: {status}')
    print()
    

def main():
    global tentativas
    global status
    gerarmatriz()
    
    

    while True:
        escolha = input('Escolha uma posição [Linha x Coluna]: ').split("x")
        try: 
            escolha[0] = int(escolha[0])-1
            escolha[1] = int(escolha[1])-1
        except(ValueError,IndexError):
            print('Escolha apenas valores númericos. Exemplo: 3x3')
            continue
        else:
            if (0 <= escolha[0] <= 4) and (0 <= escolha[1] <= 4):
                linha_escolhida = escolha[0]
                coluna_escolhida = escolha[1]
                break
            else:
                print("Escolha valores entre 1 e 5 para a linha e coluna")

    tentativas += 1

    if linha_escolhida == linha_random and coluna_escolhida == coluna_random:
        matriz[linha_escolhida][coluna_escolhida] = "T"
        status = "\033[32mParabéns! Você encontrou o tesouro!\033[m"
        return False
    else:
        matriz[linha_escolhida][coluna_escolhida] = "X"

        linha_dist = abs(linha_random - linha_escolhida)
        coluna_dist = abs(coluna_random - coluna_escolhida)

        dist = linha_dist+coluna_dist

        if dist <= 1:
            status = "Você está muito perto!"
        elif dist <= 3:
            status = "Você está perto!"
        else:
            status = "Você está longe..."

    return True

while main():
    pass

gerarmatriz()

