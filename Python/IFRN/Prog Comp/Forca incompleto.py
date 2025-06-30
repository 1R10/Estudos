from random import randint

# Define a palavra secreta
palavras = ('ABACATE', 'LIMA','ABACAXI', 'LIMAO')
segredo = palavras[randint(0, len(palavras)-1)]
visivel = '-'*len(segredo)

chances = len(segredo)//2

print(f'A palavra tem {len(segredo)} letras.')

# Loop de tentativas
while visivel != segredo:
    print(visivel)
    print(f' Você tem {chances} tentativas.')
    
    letra = input('Digite uma letra: ').upper()
    novavisivel = ''

    # Checador/substituidor de letra por letra
    for pos in range(len(segredo)):
        if letra == segredo[pos]:
            novavisivel += segredo[pos]
        else:
            novavisivel += visivel[pos]

    if letra in segredo == -1:
        chances -= 1
    



    visivel = novavisivel # transforma P-L-VR- em PALAVRA

    # Condições de vitória/derrota
    if visivel == segredo:
        print('VOCÊ VENCEU!')

        
print(f'A PALAVRA ERA {segredo}!')
