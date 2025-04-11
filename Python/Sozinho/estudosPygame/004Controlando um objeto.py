import pygame
from pygame.locals import * #* significa q dentro do submódulo "locals" eu estou importando TODAS as funções
from sys import exit #Função que será chamada para fechar a janela

pygame.init#inicializar todas as funções do pygame

#criar a tela
largura = 640
altura  = 480
tela    = pygame.display.set_mode((largura, altura)) # Uma tupla que recebe a proporção da janela


x = largura/2
y = altura/2

vel = 10

#meio = largura/2 - altura/2
pygame.display.set_caption('Teste foda') #Mudar o nome que aparece na janela
relogio = pygame.time.Clock()

while True: # O jogo PRECISA sempre estar dentro de um looping infinito
    relogio.tick(64) #define o FPS (taxa de Frame Por Segundo)
    tela.fill((0,0,0)) #apagar rastro de movimento do objeto

    for event in pygame.event.get():
        if event.type == QUIT: # Se fechar a tela vai fechar o jogo
            pygame.quit()
            exit()

        '''if event.type == KEYDOWN:
            if event.key == K_a: # A --> Esquerda
                x -= vel
            if event.key == K_d: # D --> Direita
                x += vel
            if event.key == K_w: # W --> Sobe
                y -= vel
            if event.key == K_s: # S --> Desce
                y += vel'''
    if pygame.key.get_pressed()[K_a]:
        x -= vel
    if pygame.key.get_pressed()[K_d]:
        x += vel
    if pygame.key.get_pressed()[K_w]:
        y -= vel
    if pygame.key.get_pressed()[K_s]:
        y += vel
    # Desenho de um objeto (retângulo)
    pygame.draw.rect  (tela, (255, 0, 0), (x, y, 40, 50))  #retângulo #display, RGB, x/y, altura/largura (sempre referenciada pelo canto superior esquerdo)


    pygame.display.update() #atualizar a janela
