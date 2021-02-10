import random
from time import sleep

def jogar():
    
    print("\n[ 0 ] Pedra")
    print("[ 1 ] Papel")
    print("[ 2 ] Tesoura")

    pontos_computador = 0
    pontos_usuario = 0

    while pontos_computador or pontos_usuario <= 5 + 1:

        opcoes = ("Pedra","Papel","Tesoura")
                
        usuario = int(input("\nQual é sua jogada? "))
        computador = random.randrange(0,3)

        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PO")

        print("-=" * 11)
        print("Você escolheu {}".format(opcoes[usuario]))
        print("O computador escolheu {}".format(opcoes[computador]))
        print("-=" * 11)

        if(computador == 0):
            if (usuario == 0):
                print("Empate")
            elif(usuario == 1):
                print("Você venceu!")
                pontos_usuario = pontos_usuario + 1
            elif(usuario == 2):
                print("Você perdeu!")
                pontos_computador = pontos_computador + 1
            else:
                print("Jogada Inválida")
                
        elif(computador == 1):
            if (usuario == 0):
                print("Você perdeu!")
                pontos_computador = pontos_computador + 1
            elif(usuario == 1):
                print("Empate")
            elif(usuario == 2):
                print("Você ganhou!")
                pontos_usuario = pontos_usuario + 1
            else:
                print("Jogada Inválida")
                        
        elif(computador == 2):
            if (usuario == 0):
                print("Você ganhou!")
                pontos_usuario = pontos_usuario + 1
            elif(usuario == 1):
                print("Você perdeu!")
                pontos_computador = pontos_computador + 1
            elif(usuario == 2):
                print("Empate")
            else:
                print("Jogada Inválida")

        print("\nVocê fez {} pontos de 5".format(pontos_usuario))
        print("O computador fez {} pontos de 5".format(pontos_computador))
    
        if(pontos_computador == 5):
            print("\nEu venci de você humano HAHA")
            break
        elif(pontos_usuario == 5):
            print("\nVocê venceu de mim, parabéns!")
            break
    
    input("\nPrecione uma tecla para sair")

if(__name__ == "__main__"):
    jogar()