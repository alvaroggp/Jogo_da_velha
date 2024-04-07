from utilitarios import verificando_vitoria, verificando_velha, loop_principal
from construcaoo import cabecalho, formatacao, escolha_simbolo
from jogador import jogador


continuar = True

# Cabeçalho do jogo
cabecalho()

while continuar:
    
    # Criando as posiçoes da matriz
    matriz = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    
    # Designando os simbolos personalizados 
    simbolo_1 = escolha_simbolo(1)
    simbolo_2 = escolha_simbolo(2)
    
    formatacao(matriz)

    loop_principal(matriz,simbolo_1, simbolo_2)
    
    # Perguntando se o loop deve continuar
    pergunta = input("Quer jogar novamente (sim[1]/não[2]): ")
    
    while True:

        if pergunta == "1":

            continuar = True

            break

        elif pergunta == "2":

            continuar = False

            break

        else: 

                while True:

                    pergunta = input("A reposta é invalida responda novamente (sim[1]/não[2]): ")

                    if pergunta in ["1", "2"]:

                        break
           
print("|-----Muito obrigado por ter jogado!!!-----|")
