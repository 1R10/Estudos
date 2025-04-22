import pygame
from pygame.locals import * #* significa q dentro do submódulo "locals" eu estou importando TODAS as funções
from sys import exit #Função que será chamada para fechar a janela
from random import randint
pygame.init()

#sons
'''musica_fundo = pygame.mixer.music.load('musica_fundo.mp3')
pygame.mixer.music.play(-1) #pra musica repetir é só colocar -1 no ()
pygame.mixer.music.set_volume() #valores de 0 até 1 ''' # não quero música de fundo
som_colisao  = pygame.mixer.Sound('Impacto.wav')

largura = 640
altura  = 480
tela    = pygame.display.set_mode((largura, altura))


x = int(largura/2)
y = int(altura/2)

x_verm = randint(40, 600)
y_verm = randint(50, 430)
vel = 5

pontos = 0
fonte = pygame.font.SysFont('Arial', 30, True, True) #fonte, tamanho, negrito e itálico

pygame.display.set_caption('Teste foda')
relogio = pygame.time.Clock()

while True:
    relogio.tick(64)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Movimento WASD    
    if pygame.key.get_pressed()[K_a]:
        x -= vel
    if pygame.key.get_pressed()[K_d]:
        x += vel
    if pygame.key.get_pressed()[K_w]:
        y -= vel
    if pygame.key.get_pressed()[K_s]:
        y += vel

    # Objetos
    qua_azul      = pygame.draw.rect  (tela, (0, 0, 255), (x, y, 20, 20))
    ret_verm = pygame.draw.rect  (tela, (255, 0, 0), (x_verm, y_verm, 40, 50)) 
    # Colisão
    if qua_azul.colliderect(ret_verm):
        print('BATEU AI AI PARA')
        x_verm = randint(40, 600)
        y_verm = randint(50, 430)
        pontos = pontos + 1
        som_colisao.play()
    
    tela.blit(texto_formatado, (10, 10))
    pygame.display.update() #atualizar a janela
