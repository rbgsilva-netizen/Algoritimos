import os

# matriz = [["███" if (j+i) % 2 == 0 else "   " for j in range(8)] for i in range(8)]
matriz = [[" . " for j in range(8)] for i in range(8)]
movimentos = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
cred = "\033[31m"
cgreen = "\033[32m"
cyel = "\033[33m"
cblue = "\033[34m"
cz = "\033[m"


def gerarmatriz():
    os.system("cls")

    print("Xadrez".center(30))
    print("="*30)

    print("   ", end="")
    for i in range(8):
        print(f"{cyel}{i:^3}{cz}", end="")
    print("\n")

    for k, v in enumerate(matriz):
        print(f"{cyel}{k:<3}{cz}", end="")
        for j in v:
            print(f"{j}", end="")
        print()
    print()


def main():
    gerarmatriz()
    while True:
        try:
            escolha = input("Escolha uma posição [linha x coluna]: ").split("x")
            linha_escolhida = int(escolha[0])
            coluna_escolhida = int(escolha[1])
        except (ValueError, IndexError):
            print("Entrada invlálida. Tente novamente. Exemplo: 3x4")
            continue
        else:
            if (0 <= linha_escolhida <= 7) and (0 <= coluna_escolhida <= 7):
                break
            else:
                print("Coordenada inválida. Minimo 0x0. Máximo 7x7.")
                continue

    matriz[linha_escolhida][coluna_escolhida] = "\033[32m C \033[m"

    for x, y in movimentos:
        posx = linha_escolhida + x
        posy = coluna_escolhida + y
        
        if 0 <= posx <= 7 and 0 <= posy <= 7:
            matriz[posx][posy] = "\033[32m * \033[m"

    gerarmatriz()

main()