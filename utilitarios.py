def cabecalho():
    print("|-----------------------|")
    print("|-----Jogo-da-velha-----|")
    print("|-----------------------|")



def escolha_simbolo(j):
    if j == 1:
        simbolo = input("Qual o simbolo que o jogador numero 1 deseja utilizar: ")
    
    else:
        simbolo = input("Qual o simbolo que o jogador numero 2 deseja utilizar: ")

        if len(simbolo) > 1 :
                while True:
                    
                    simbolo_1 = str(input("Infelizmente o Simbolo escolhido é invalido, por favor escolha outro: "))
                    
                    if len(simbolo) == 1:
                        break
                    break
    return simbolo



def formatacao(matriz):
    print(f" {matriz[0]} | {matriz[1]} | {matriz[2]}")
    print("---|---|---")
    print(f" {matriz[3]} | {matriz[4]} | {matriz[5]}")
    print(("---|---|---"))
    print(f" {matriz[6]} | {matriz[7]} | {matriz[8]}")
    


def jogadores(j, matriz, simbolo_x, simbolo_y):            
    jogador = int(input(f"Qual posição o Jogador {j} deseja jogar: "))
    
    if matriz[jogador] == simbolo_y or matriz[jogador] == simbolo_x or 0 >jogador > 8:

        while True:
            
            jogador = int(input("A resposta não é valida, tente novamente: "))
              
    else:
    
        matriz[jogador] = simbolo_x
    
    formatacao(matriz)

    
    

def verificando_vitoria(j, matriz, simbolo_x):
    if any(all(matriz[i] == simbolo_x for i in sublista) for sublista in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], 
    [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]):
        
        print(f"O jogador {j} venceu!!!")
        return True

    else:
        return False 
        


def verificando_velha(contador):
    print(contador)
    if contador ==  8:
        
        print("DEU VELHA!!!")
        return True



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
        