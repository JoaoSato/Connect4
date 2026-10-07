tabuleiro = [
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", "O", " "],
    [" ", " ", " ", " ", "O", " ", " "],
    [" ", " ", " ", "O", " ", " ", " "],
    [" ", "O", " ", " ", " ", " ", " "]
]

def imprimir_tabuleiro(tabuleiro):
    print("    1   2   3   4   5   6   7")
    print("  +---+---+---+---+---+---+---+")

    numero_linha = 1
    for linha in tabuleiro:
        imp_linha = ""
        for coluna in linha:
            imp_linha += coluna + " | "

        print(f'{numero_linha} | {imp_linha}')
        print(f'  +---+---+---+---+---+---+---+')

        numero_linha += 1

def jogada(tab,peca):
    print(f'Turno das peças {peca}.')
    play = int(input("Digite onde jogar uma peça na coluna 1 a 7: "))-1

    invalido = True
    while invalido == True:
        if play < 0 or play > 6:
            print("Essa coluna não existe!")
            play = int(input("Digite onde jogar uma peça na coluna 1 a 7: "))-1
        else:
            if tab[1][play] != " ":
                print("Coluna cheia! Faça outra jogada!")
                play = int(input("Digite onde jogar uma peça na coluna 1 a 7: "))-1
            else:
                invalido = False

    """ for i in range(len(tab)-1, -1, -1):
        if tab[i][play] == " ":
            tab[i][play] = peca
            break """

    posicao = None
    for c in range(len(tab)):
        if tab[c][play] == " ":
            posicao = c

    tab[posicao][play] = peca

    imprimir_tabuleiro(tab)

def verificar_vitoria_horizontal(tab, peca):

    for i in range(6):
        for j in range(4):
            if tab[i][j] == peca and tab[i][j+1] == peca and tab[i][j+2] == peca and tab[i][j+3] == peca:
                print(f'Vitória do {peca} :)')
                return True
    return False

def verificar_vitoria_vertical(tab, peca):
    for i in range(3):
            for j in range(7):
                if tab[i][j] == peca and tab[i+1][j] == peca and tab[i+2][j] == peca and tab[i+3][j] == peca:
                    print(f'Vitória do {peca} :)')
                    return True
    return False

def verificar_vitoria_diagonal_direita(tab, peca):
    for i in range(3):
        for j in range(4):
            if tab[i][j] == peca and tab[i+1][j+1] == peca and tab[i+2][j+2] == peca and tab[i+3][j+3] == peca:
                print(f'Vitória do {peca} :)')
                return True
    return False

def verificar_vitoria_diagonal_esquerda(tab, peca):
    for i in range(3):
        for j in range(3, 7):
            if tab[i][j] == peca and tab[i+1][j-1] == peca and tab[i+2][j-2] == peca and tab[i+3][j-3] == peca:
                print(f'Vitória do {peca} :)')
                return True
    return False



#Main
peca = "O"
imprimir_tabuleiro(tabuleiro)

jogada(tabuleiro, peca)

vit_horizontal = verificar_vitoria_horizontal(tabuleiro, peca)
vit_vertical = verificar_vitoria_vertical(tabuleiro, peca)
vit_diag_direita = verificar_vitoria_diagonal_direita(tabuleiro, peca)
vit_diag_esquerda = verificar_vitoria_diagonal_esquerda(tabuleiro, peca)


def gameplay(tab):
    pecas = ["X", "O"]
    vitoria = False

    while vitoria == False:
        jogada(tab, peca)
        vit_horizontal = verificar_vitoria_horizontal(tab, peca)
        vit_vertical = verificar_vitoria_vertical(tab, peca)
        vit_diag_direita = verificar_vitoria_diagonal_direita(tab, peca)
        vit_diag_esquerda = verificar_vitoria_diagonal_esquerda(tab, peca)

        if (vit_horizontal or vit_vertical or
            vit_diag_direita or vit_diag_esquerda):

            vitoria = True

        elif jogadas == 42:
            print("Empate! O tabuleiro está cheio.")
            vitoria = True

        else:
            if peca == "O":
                peca = "X"
            else:
                peca = "O"

# Main
imprimir_tabuleiro(tabuleiro)
gameplay(tabuleiro)