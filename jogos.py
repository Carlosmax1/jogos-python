import advinhacao
import forca
import jokenpo

def escolher_jogo(): 
    #teste
    print("********************************")
    print("Escolhe o seu jogo!")
    print("********************************")

    print("(1) Forca (2) Advinhação (3) Jokenpo")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando advinhação")
        advinhacao.jogar()
    elif(jogo == 3):
        print("Jogando Jokenpo")
        jokenpo.jogar()

escolher_jogo()