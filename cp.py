tabuleiro = [["X", " ", " ", " ", " ", " ", " "],
             ["X", " ", " ", " ", " ", " ", " "],
             ["X", " ", " ", " ", " ", " ", " "],
             ["X", " ", " ", " ", " ", " ", " "],
             ["X", " ", " ", " ", " ", " ", "X"],
             ["O", "O", " ", " ", " ", " ", "X"]]

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
    print(f'Turno das peças {peca} .')
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

jogada(tabuleiro,"X")