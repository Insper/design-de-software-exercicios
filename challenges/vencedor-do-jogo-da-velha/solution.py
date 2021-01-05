def verifica_jogo_da_velha(tabuleiro):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if(tabuleiro[i][0]==tabuleiro[i][1]==tabuleiro[i][2]=='X' or tabuleiro[0][j]==tabuleiro[1][j]==tabuleiro[2][j]=='X' or tabuleiro[0][0]==tabuleiro[1][1]==tabuleiro[2][2]=='X' or tabuleiro[0][2]==tabuleiro[1][1]==tabuleiro[2][0]=='X'):
                return 'X'
            elif(tabuleiro[i][0]==tabuleiro[i][1]==tabuleiro[i][2]=='O' or tabuleiro[0][j]==tabuleiro[1][j]==tabuleiro[2][j]=='O' or tabuleiro[0][0]==tabuleiro[1][1]==tabuleiro[2][2]=='O' or tabuleiro[0][2]==tabuleiro[1][1]==tabuleiro[2][0]=='O'):    
                return 'O'
    return 'V'
