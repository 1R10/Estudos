import pygame
from pygame.locals import * #* significa q dentro do submódulo "locals" eu estou importando TODAS as funções
from sys import exit #Função que será chamada para fechar a janela
from random import randint
pygame.init()

#sons
'''musica_fundo = pygame.mixer.music.load('musica_fundo.mp3')
pygame.mixer.music.play(-1) #pra musica repetir é só colocar -1 no ()
pygame.mixer.music.set_volume() #valores de 0 até 1 ''' # não quero música de fundo
som_colisao  = pygame.mixer.Sound('Impacto.wav') #arquivo precisa estar em nome.wav

largura = 640
altura  = 480
tela    = pygame.display.set_mode((largura, altura))


x_cobra = int(largura/2)
y_cobra = int(altura/2)

x_fruta = randint(40, 600)
y_fruta = randint(50, 430)
vel = 5

pontos = 0
fonte = pygame.font.SysFont('Arial', 30, True, True) #fonte, tamanho, negrito e itálico

pygame.display.set_caption('Teste foda')
relogio = pygame.time.Clock()

lista_cobra = []
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:

        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))

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
        x_cobra -= vel
    if pygame.key.get_pressed()[K_d]:
        x_cobra += vel
    if pygame.key.get_pressed()[K_w]:
        y_cobra -= vel
    if pygame.key.get_pressed()[K_s]:
        y_cobra += vel

    # Objetos
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    fruta = pygame.draw.rect(tela, (255, 0, 0), (x_fruta, y_fruta, 20, 20)) 
   
    # Colisão
    if cobra.colliderect(fruta):
        print('colidiu')
        x_fruta = randint(40, 600)
        y_fruta = randint(50, 430)
        pontos = pontos + 1
        som_colisao.play()
        aumenta_cobra(lista_cobra)


    # Desenho da cobra
    lista_cabeca = []
    lista_cabeca.append(x_cobra) #, y_cobra
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    #aumenta_cobra(lista_cobra)


    tela.blit(texto_formatado, (10, 10))
    pygame.display.update() #atualizar a janela
