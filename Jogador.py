def jogadores(j, matriz, simbolo_x, simbolo_y):            
    jogador = int(input(f"Qual posição o Jogador {j} deseja jogar: "))
    
    if matriz[jogador] == simbolo_y or matriz[jogador] == simbolo_x or 0 >jogador > 8:

        while True:
            
            jogador = int(input("A resposta não é valida, tente novamente: "))
              
    else:
    
        matriz[jogador] = simbolo_x
    
    formatacao(matriz)