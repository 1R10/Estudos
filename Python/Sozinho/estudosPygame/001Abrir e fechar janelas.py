import pygame
from pygame.locas import * #* significa q dentro do submódulo "locals" eu estou importando TODAS as funções
from sys import exit #Função que será chamada para fechar a janela

pygame.init#inicializar todas as funções do pygame

#criar a tela
largura = 640
altura  = 480
tela    = pygame.display.set_mode((largura, altura)) # Uma tupla que recebe a proporção da janela

# O jogo PRECISA sempre estar dentro de um looping infinito

While True:

  for event un pygame.event.get():
    if event.type == QUIT: # Se fechar a tela vai fechar o jogo
      pygame.quit()
      exit()
      
    pygame.display.update() #atualizar a janela
