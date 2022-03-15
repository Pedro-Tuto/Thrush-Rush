import pygame
import sys
import time
import random

#definindo as dimensões da janela
LARGURA = 1500
ALTURA = 1000

#definindo as cores
preto = (0,0,0)
branco = (255,255,255)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
azul_claro = (0,100,200)

#a largura em pixels da imagem para uso posterior
largura_passaro = 295

#iniciando o pygame e definindo o clock
pygame.init()
gameDisplay = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Thrush Rush')
clock = pygame.time.Clock()


#definindo os obstáculos
def obstaculos(thingx, thingy, thingl, thinga, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingl, thinga])



#inserindo a imagem do pássaro e definindo suas coordenadas
thrushimg = pygame.image.load("bird.png")
def bird(x,y):
    gameDisplay.blit(thrushimg,(x,y))

#definindo o objeto de texto
def text_objects(text, font):
    textoSuperficie = font.render(text, True, vermelho)
    return textoSuperficie, textoSuperficie.get_rect()


#definindo as mensagens que podem aparecer no jogo
def mensagem_display(text):
    textoGrande = pygame.font.Font('freesansbold.ttf', 115)
    textoSurperficie, textoRetangulo = text_objects(text, textoGrande)
    #centralizando a caixa de texto
    textoRetangulo.center = ((LARGURA//2, ALTURA//2))
    #fazendo a mensagem aparecer com .blit
    gameDisplay.blit(textoSurperficie, textoRetangulo)
    pygame.display.update()
    #criando um tempo antes de o jogo reiniciar
    time.sleep(2)
    #reiniciando o jogo chamando o main()
    main()


#definindo o que acontece quando o jogador bate
def crash():
    mensagem_display('Você Bateu')


def main():
    
    x = (LARGURA * 0.38)
    y = (ALTURA * 0.70)

    x_move = 0

    #definindo onde os obstáculos aparecem
    obstaculo_startx = random.randrange(0, LARGURA)
    obstaculo_starty = -600
    #definindo a velocidade dos obstáculos
    obstaculo_speed = 7
    #definindo a largura e altura do obstáculos
    obstaculo_width = 100
    obstaculo_height = 100



    #criando o main loop do jogo
    gameEnd = False
    while not gameEnd:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #configurando os inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = -100
                elif event.key == pygame.K_RIGHT:
                    x_move = 100
            #configurando o que acontece quando soltamos a tecla
            if event.type == pygame.KEYUP:   
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_move = 0
            x += x_move
        #preenchendo o fundo com azul claro
        gameDisplay.fill(azul_claro)

        #obstaculos(thingx, thingy, thingl, thinga, color)
        obstaculos(obstaculo_startx, obstaculo_starty, obstaculo_width, obstaculo_height, branco)
        #para mover verticalmente o obstaculo
        obstaculo_starty += obstaculo_speed

        #chamando o pássaro
        bird(x,y)
        
        #usando x = 0 e a largura da tela subtraída da imagem para definir se o passaro bate nas bordas da janela ou nao
        if x > LARGURA - largura_passaro or x < 0:
            crash()
        
        #definindo se os obstaculos estão fora da tela resetando sua altura em y e randozimando sua posição em x
        if obstaculo_starty > ALTURA:
            obstaculo_starty = 0 - obstaculo_height
            obstaculo_startx = random.randrange(0, LARGURA)

        #updatando para mostrar na tela todas as imagens
        pygame.display.update()
        clock.tick(60)

        print(event)

    pygame.quit()
    sys.exit()

main()


