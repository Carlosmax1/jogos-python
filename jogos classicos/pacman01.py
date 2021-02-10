import pygame

amarelo = (255,255,0)
preto = (0,0,0)
velocidade = 0.0001
raio = 30
pygame.init()


tela = pygame.display.set_mode((640,480),0)
x = 10
y = 10
velocidade_x = velocidade
velocidade_y = velocidade


while True:
            #Calcula regras
            
            x += velocidade_x
            y += velocidade_y

            if x + raio > 640:
                        velocidade_x -= velocidade

            if x - raio < 0:
                        velocidade_x += velocidade
            
            if y + raio > 480:
                        velocidade_y -= velocidade
            
            if y - raio < 0:
                        velocidade_y += velocidade

            # Pinta a tela
           
           
            tela.fill((preto))
            pygame.draw.circle(tela,amarelo, (int(x),int(y)), raio, 0)
            pygame.display.update()
            
            
            # Eventos do usuário
            for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                                    exit()

# Imprimindo objetos na tela com a lib Pygame