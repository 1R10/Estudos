import pygame
from pygame.locals import * #* significa q dentro do submódulo "locals" eu estou importando TODAS as funções
from sys import exit #Função que será chamada para fechar a janela

pygame.init#inicializar todas as funções do pygame

#criar a tela
largura = 640
altura  = 480
tela    = pygame.display.set_mode((largura, altura)) # Uma tupla que recebe a proporção da janela

pygame.display.set_caption('Meu primeiro display') #Mudar o nome que aparece na janela

while True: # O jogo PRECISA sempre estar dentro de um looping infinito
    for event in pygame.event.get():
        if event.type == QUIT: # Se fechar a tela vai fechar o jogo
            pygame.quit()
            exit()

    # Desenho de um pixel
    pygame.draw.rect  (tela, (255, 0, 0), (200, 300, 40, 50))  #retângulo #display, RGB, x/y, altura/largura (sempre referenciada pelo canto superior esquerdo)
    pygame.draw.circle(tela, (0, 0, 255), (300, 260), 40)      #circulo   #display, RGB, x/y, raio(tamanho) do círculo
    pygame.draw.line  (tela, (0, 255, 0), (390,0), (390, 600)) #linha     #display, RGB, posição x, posição y
     
    pygame.display.update() #atualizar a janela
