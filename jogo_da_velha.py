from utilitarios import loop_principal, repetir
from construcao import cabecalho, escolha_simbolo, formatacao

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
    continuar = repetir()
    
               
print("|-----Muito obrigado por ter jogado!!!-----|")