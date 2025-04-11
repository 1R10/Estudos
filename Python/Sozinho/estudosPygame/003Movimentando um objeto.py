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


#meio = largura/2 - altura/2
pygame.display.set_caption('Meu primeiro display') #Mudar o nome que aparece na janela
relogio = pygame.time.Clock()

while True: # O jogo PRECISA sempre estar dentro de um looping infinito
    relogio.tick(64) #define o FPS (taxa de Frame Por Segundo)
    tela.fill((0,0,0)) #apagar rastro de movimento do objeto

    for event in pygame.event.get():
        if event.type == QUIT: # Se fechar a tela vai fechar o jogo
            pygame.quit()
            exit()

    # Desenho de um objeto (retângulo)
    pygame.draw.rect  (tela, (255, 0, 0), (x, y, 40, 50))  #retângulo #display, RGB, x/y, altura/largura (sempre referenciada pelo canto superior esquerdo)
    if y >= altura:
        y = 0
    if x >= largura:
        x = 0    
    y = y + 1
    x


    pygame.display.update() #atualizar a janela
