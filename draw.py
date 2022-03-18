import pygame

pygame.init

preto = (0,0,0)
branco = (255,255,255)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
azul_claro = (0,100,200)

gameDisplay = pygame.display.set_mode((800,800))
gameDisplay.fill(preto)

#usando os pixels da janela para desenhar um ponto
pixAr = pygame.PixelArray(gameDisplay)
pixAr [10] [20] = verde
#desenhando linhas (local, cor, coordenada_inicial, coordenada_final, grossura de pixels)
pygame.draw.line(gameDisplay, azul, (100,200), (300,450), 10)
#desenhando retângulos (especificamos o x e y da diagonal superior esquerda, e depois especificamos a largura e altura)
pygame.draw.rect(gameDisplay, vermelho, (400,400,50,50))
#desenhando círculos (especificamos o centro do círculo e o raio)
pygame.draw.circle(gameDisplay, branco, (150,150), 75)
#desenhando qualquer polígono
pygame.draw.polygon(gameDisplay, verde, ((25,75), (76,125), (250,375), (400,25)))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()