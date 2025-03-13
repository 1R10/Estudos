import random
pc = random.randint(0,10)
#print(pc)
n = 11
palpite = 1
while n != pc:
    n = int(input('\nAdvinhe o valor entre 0 e 10 que o PC sorteou: '))
    if n != pc:
        print('\nVocê errou!')
        palpite += 1
    else:
        break
print(f'Parabéns! O valor era {pc}. Você precisou de {palpite} palpites.\n\n Encerrando o programa...')