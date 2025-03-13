import random, time
from random import randint
while True:
    objetos = ('Pedra', 'Papel', 'Tesoura')
    escolhaComputador = randint(0, 2)
    escolhaJogador = int(input('Escolha entre Pedra, Papel ou Tesoura (0, 1 ou 2): '))
    if escolhaJogador < 0  or escolhaJogador > 2:
        print('ESCOLHA UM NÚMERO ENTRE 0 E 2.')
    else:
        print(escolhaComputador,'\n',escolhaJogador)
        #em obras

    