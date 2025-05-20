frase = str(input('Digite uma frase: '))
letra = str(input('Digite qual letra ou número você quer encontrar na frase\n(Se colocar uma sequência, vai ser procurada uma sequência): '))

quantidade = frase.strip().upper().count(letra.upper())
primeira   = frase.upper().find(letra.upper()) + 1
ultima     = frase.upper().rfind(letra.upper()) + 1

print(f'Na frase "{frase}", "{letra}" aparece {quantidade} vezes.')
print(f'Primeira ocorrência na {primeira}° posição')
print(f'Última ocorrência na {ultima}° posição.')