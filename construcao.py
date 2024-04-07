def cabecalho():
    print("|-----------------------|")
    print("|-----Jogo-da-velha-----|")
    print("|-----------------------|")


def formatacao(matriz):
    print(f" {matriz[0]} | {matriz[1]} | {matriz[2]}")
    print("---|---|---")
    print(f" {matriz[3]} | {matriz[4]} | {matriz[5]}")
    print(("---|---|---"))
    print(f" {matriz[6]} | {matriz[7]} | {matriz[8]}")
    

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
