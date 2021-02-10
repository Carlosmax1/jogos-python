import random

def jogar():

    print("********************************")
    print("Bem vindo ao jogo de Advinhação!")
    print("********************************")

    total_de_tentativas = 0
    #numero_secreto = round(random.random() * 100)  numero entre 0.0 e 1.0
    numero_secreto = random.randrange(1,101)
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Díficil")

    nivel = int(input("\nDefina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for tentativas in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(tentativas, total_de_tentativas))

        chute_str = input("Digite um numero entre 1 e 100: ")
        chute = int(chute_str)

        if(chute > 100 or chute < 1):
            print("Digite um numero entre 1 e 100")
            continue

        print("Você digitou o número: ", chute_str, end="\n")

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos :)".format(pontos))
            break
        else:
            if(maior):
                print("Você errou, o seu chute foi maior que o número secreto")
            elif(menor):
                print("Você errou, o seu chute foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo")
    print("O numero secreto era {}.".format(numero_secreto))


if(__name__ == "__main__"):
    jogar()