from utilitarios import formatacao


continuar = True
contador = 0

# Cabeçalho do jogo
print("|-----Jogo-da-velha-----|\n")

while continuar:
    
    # Criando as posiçoes da matriz
    matriz = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    
    # Designando os simbolos personalizados
    while True:
            
            simbolo_1 = str(input("Qual simbolo o Jogador 1 quer usar: "))
            
            if len(simbolo_1) > 1 :
                while True:
                    
                    simbolo_1 = str(input("Infelizmente o Simbolo escolhido é invalido, por favor escolha outro: "))
                    
                    if len(simbolo_1) == 1:
                        break

            simbolo_2 = str(input("Qual simbolo o jogador 2 quer usar: "))

            if len(simbolo_2) > 1 or simbolo_2 == simbolo_1:
                while True:
                    
                    simbolo_2 = str(input("Infelizmente o Simbolo escolhido é invalido, por favor escolha outro: "))
                    
                    if len(simbolo_2) == 1 and simbolo_2 != simbolo_1:
                        break

            else:
                break
    
    # Loop central do jogo
    while True:

        # Chamando a formatação da matriz
        formatacao(matriz)
        
        # Codigo referente ao Jogador 1
        jogador_1 = int(input("Qual posição o Jogador 1 deseja jogar: "))
        
        if matriz[jogador_1] == simbolo_2 or matriz[jogador_1] == simbolo_1 or 0 >jogador_1 > 8:

            while True:
                
                jogador_1 = int(input("A resposta não é valida, tente novamente: "))
                
                if matriz[jogador_1] ==simbolo_2 or matriz[jogador_1] == simbolo_1:
                    continue

                else: 
                    matriz[jogador_1] = simbolo_1
                    break
        else:
        
            matriz[jogador_1] = simbolo_1

        formatacao(matriz)

        if any(all(matriz[i] == simbolo_1 for i in sublista) for sublista in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], 
        [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]):

            print("jogador 1 venceu!!!")

            break
        
        contador += 1

        if contador == 9:

            print("Deu velha!!!")

            break

        # Codigo referente ao Jogador 2
        jogador_2 = int(input("Qual posição o Jogador 2 deseja jogar: "))

        if matriz[jogador_2] == simbolo_2 or matriz[jogador_2] == simbolo_1 or 0 > jogador_2 > 8:
            
            while True:

                jogador_2 = int(input("A resposta não é valida, tente novamente: "))

                if matriz[jogador_2] == simbolo_2 or matriz[jogador_2] == simbolo_1:

                    continue

                else: 

                    matriz[jogador_2] = simbolo_2

                    break
    
        matriz[jogador_2] = simbolo_2

        if any(all(matriz[i] == simbolo_2 for i in sublista) for sublista in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], 
        [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]):

            print("jogador 2 venceu!!!")

            break

        contador += 1
    
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
