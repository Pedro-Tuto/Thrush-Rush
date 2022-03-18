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
vermelho = (200,0,0)
vermelho_claro = (255,0,0)
verde = (0,200,0)
verde_claro = (0,255,0)
azul = (0,0,255)
azul_claro = (0,100,200)
roxo = (221,160,221)


#definindo a contagem dos obstáculos que foram desviados
def obstaculos_dodged(count):
    font = pygame.font.SysFont(None, 100)
    text = font.render('Dibrados: ' + str(count), True, verde)
    gameDisplay.blit(text, (0,0))


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
    textoSuperficie = font.render(text, True, preto)
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

#definindo a função dos botões
def button(msg, x, y, w, h, ic, ac, action = None):

    mouse = pygame.mouse.get_pos()
    #print(mouse) 
    #definindo o clique
    click = pygame.mouse.get_pressed()
    #print(click)

    #se a coordenada x do retangulo + a largura for maior que o valor x da posição do mouse
    #E a coordenada y do retangulo + a altura for maior que o valor y da posição do mouse
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            if action == 'play':
                main()
            elif action == 'quit':
                pygame.quit()
                sys.exit()

    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
    #inserindo texto no botão
    textoPequeno = pygame.font.Font("freesansbold.ttf", 50)
    textoSurperficie, textoRetangulo = text_objects(msg, textoPequeno)
    #centralizando utilizando x e largura
    textoRetangulo.center = ((x+(w/2)), (y +(h/2)))
    #fazendo o texto aparecer
    gameDisplay.blit(textoSurperficie, textoRetangulo)
    
#definindo o que acontece quando o jogador bate
def crash():
    mensagem_display('Você Bateu')

#----------------------------------------------------------------------------------------------------------------------------------------------------
#definindo o menu do jogo
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        gameDisplay.fill(roxo)
        textoGrande = pygame.font.Font('freesansbold.ttf', 115)
        textoSurperficie, textoRetangulo = text_objects("THRUSH RUSH!", textoGrande)
        #centralizando a caixa de texto
        textoRetangulo.center = ((LARGURA//2, ALTURA//2))
        #fazendo a mensagem aparecer com .blit
        gameDisplay.blit(textoSurperficie, textoRetangulo)

        #chamando a função botão e escolhemos os parâmetros
        button("START", 155,700,400,200,verde,verde_claro,'play')
        button("QUIT", 955,700,400,200,vermelho,vermelho_claro,'quit')

        


        pygame.display.update()
        clock.tick(15)  

#---------------------------------------------------------------------------------------------------------------------------------------------------

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
    obstaculo_width = 200
    obstaculo_height = 100
    dodged = 0

    #criando o main loop do jogo
    gameEnd = False
    while not gameEnd:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x += -30
        elif keys[pygame.K_RIGHT]:
            x += 30

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        '''for event in pygame.event.get():
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
            x += x_move'''
            
        #preenchendo o fundo com azul claro
        gameDisplay.fill(azul_claro)

        #obstaculos(thingx, thingy, thingl, thinga, color)
        obstaculos(obstaculo_startx, obstaculo_starty, obstaculo_width, obstaculo_height, branco)
        #para mover verticalmente o obstaculo
        obstaculo_starty += obstaculo_speed

        #chamando o pássaro
        bird(x,y)

        #definindo número de obstaculos desviados
        obstaculos_dodged(count=dodged)
        
        #usando x = 0 e a largura da tela subtraída da imagem para definir se o passaro bate nas bordas da janela ou nao
        if x > LARGURA - largura_passaro or x < 0:
            crash()
        
        #definindo se os obstaculos estão fora da tela resetando sua altura em y e randozimando sua posição em x
        if obstaculo_starty > ALTURA:
            obstaculo_starty = 0 - obstaculo_height
            obstaculo_startx = random.randrange(0, LARGURA)
            #registrando o numero de desvios
            dodged += 1
            #aumentando a velocidade a cada desvio
            obstaculo_speed += 0.3
            #aumentando/diminuindo o tamanho dos obstáculos
            if dodged in range(10,20):
                obstaculo_width += (dodged*1)
            if dodged > 40:
                obstaculo_width = 50

        #definindo a colisão dos obstaculos
        if y < obstaculo_starty + obstaculo_height:
            print('colisão em y')
            if x + largura_passaro > obstaculo_startx and x < obstaculo_startx + obstaculo_width:
                 print('colisão em x')
                 crash()

        #updatando para mostrar na tela todas as imagens
        pygame.display.update()
        clock.tick(60)
        print(clock.get_fps())

        
    pygame.quit()
    sys.exit()

game_intro()
main()


