from construcao import formatacao

# Verificando se o um dos jogadores venceu 
def verificando_vitoria(j, matriz, simbolo_x):
    if any(all(matriz[i] == simbolo_x for i in sublista) for sublista in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], 
    [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]):
        
        print(f"O jogador {j} venceu!!!")
        return True

    else:
        return False 
        

# Verificando se o resultado da partida foi velha
def verificando_velha(contador):
    if contador ==  8:
        
        print("DEU VELHA!!!")
        return True

# Codigo referente aos jogadores
def jogadores(j, matriz, simbolo_x, simbolo_y):            
    jogador = int(input(f"Qual posição o Jogador {j} deseja jogar: "))
    
    if matriz[jogador] == simbolo_y or matriz[jogador] == simbolo_x or 0 >jogador > 8:

        while True:
            
            jogador = int(input("A resposta não é valida, tente novamente: "))
              
    else:
    
        matriz[jogador] = simbolo_x
    
    formatacao(matriz)



# Codigo referente ao loop pricipal
def loop_principal(matriz, simbolo_1, simbolo_2):
    contador = 0
    while True:
        jogadores(1, matriz, simbolo_1, simbolo_2)
        venceu_1 = verificando_vitoria(1, matriz, simbolo_1)
        if venceu_1: break
        
        velha = verificando_velha(contador)
        contador += 1
        if velha: break
        
        jogadores(2, matriz, simbolo_2, simbolo_1)
        venceu_2 = verificando_vitoria(2, matriz, simbolo_2)
        if venceu_2: break
        
        velha = verificando_velha(contador)
        contador += 1
        if velha: break
        

# Codigo responsavel pela pergunta de continuar com o jogo
def repetir():
    pergunta = input("Quer jogar novamente (sim[1]/não[2]): ")

    while True:
    
        if pergunta == "1":

            continuar = True

            return continuar
            
            break 

        elif pergunta == "2":

            continuar = False

            return continuar
            
            break

        else: 

            while True:

                pergunta = input("A reposta é invalida responda novamente (sim[1]/não[2]): ")

                if pergunta in ["1", "2"]:

                    break