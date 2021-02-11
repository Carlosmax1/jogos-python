import pygame

pygame.init()

screen = pygame.display.set_mode((800,600), 0)

amarelo = (255,255,0)
azul = (0,0,255)
preto = (0,0,0)
velocidade = 1

class Cenario: # Cria o cenário

            def __init__(self, tamanho): # 
                        self.tamanho = tamanho
                        self.matriz = [ # Matriz responsavel pela criação do cenário
                        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                        [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                        [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                        [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
                        [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
                        [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
                        [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                        [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                        [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
                        [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
                        [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
                        [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                        [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                        [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                        [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
                        ]
            def pintar_linha(self,tela, numero_linha, linha):
                        
                        for numero_coluna, coluna in enumerate(linha): # Pinta cada linha e coluna
                                    x = numero_coluna * self.tamanho   # De acordo com o calculo numero_linha * tamanho do cenario
                                    y = numero_linha * self.tamanho 
                                    half = self.tamanho // 2
                                    cor = preto
                                    if(coluna == 2):
                                                cor = azul
                                    pygame.draw.rect(tela, cor,(x, y, self.tamanho, self.tamanho), 0) # Desenha os retângulos
                                    if(coluna == 1):
                                                pygame.draw.circle(tela, amarelo,(x + half, y + half),self.tamanho // 10, 0)

            def pintar(self, tela):
                        
                        for numero_linha, linha in enumerate(self.matriz):
                                     self.pintar_linha(tela, numero_linha ,linha) # pega cada coluna e linha


class Pacman:
            def __init__(self, tamanho):
            
                        self.linha = 1
                        self.coluna = 1
                        self.centro_x = 400 
                        self.centro_y = 300
                        self.tamanho = tamanho
                        self.raio = self.tamanho // 2
                        self.velocidade_x = 0
                        self.velocidade_y = 0

            def calcular_regras(self):
                       
                        self.coluna += self.velocidade_x
                        self.linha += self.velocidade_y
                        self.centro_x = int(self.coluna * self.tamanho + self.raio)
                        self.centro_y = int(self.linha * self.tamanho + self.raio)

            def processar_eventos(self, eventos):

                        for e in eventos:
                                    if e.type == pygame.KEYDOWN: 
                                                if e.key == pygame.K_RIGHT:
                                                            self.velocidade_x = velocidade
                                    
                                    if e.type == pygame.KEYUP:
                                                if e.key == pygame.K_RIGHT:
                                                            self.velocidade_x = 0
                                    
                                    if e.type == pygame.KEYDOWN:
                                                if e.key == pygame.K_LEFT:
                                                            self.velocidade_x = -velocidade
                                    if e.type == pygame.KEYUP:
                                                if e.key == pygame.K_LEFT:
                                                            self.velocidade_x = 0
                                    
                                    if e.type == pygame.KEYDOWN:
                                                if e.key == pygame.K_UP:
                                                            self.velocidade_y = -velocidade
                                    if e.type == pygame.KEYUP:
                                                if e.key == pygame.K_UP:
                                                            self.velocidade_y = 0
                                    if e.type == pygame.KEYDOWN:
                                                if e.key == pygame.K_DOWN:
                                                            self.velocidade_y = velocidade
                                    if e.type == pygame.KEYUP:
                                                if e.key == pygame.K_DOWN:
                                                            self.velocidade_y = 0


            def pintar(self, tela):

                        #Desenhar corpo do pacman
                        pygame.draw.circle(tela,amarelo,(self.centro_x, self.centro_y), self.raio, 0)

                        #Desenho da boca
                        canto_boca = (self.centro_x, self.centro_y)
                        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
                        labio_inferior = (self.centro_x + self.raio, self.centro_y)
                        pontos = [canto_boca,labio_superior,labio_inferior]
                        pygame.draw.polygon(tela, preto, pontos, 0)

                        #Desenhando o olho
                        olho_x = int(self.centro_x + self.raio / 3)
                        olho_y = int(self.centro_y - self.raio * 0.70)
                        olho_raio = int(self.raio / 10)
                        pygame.draw.circle(tela,preto,(olho_x,olho_y),olho_raio, 0)

if __name__ == '__main__':
            size = 600 // 30
            pacman = Pacman(size)
            cenario = Cenario(size)

            while True:
                        #Calcular as regras
                        pacman.calcular_regras()

                        #Pintar tela
                        screen.fill(preto)
                        cenario.pintar(screen)
                        pacman.pintar(screen)
                        pygame.display.update()
                        pygame.time.delay(100)


                        #Captura os eventos
                        eventos = pygame.event.get()
                        pacman.processar_eventos(eventos)
                        for e in eventos:
                                    if e.type == pygame.QUIT:
                                                exit()
