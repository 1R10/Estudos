nota_um   = int(input('Primeira nota: '))
nota_dois = int(input('Segunda nota: '))

media = (nota_um + nota_dois)/2

if media < 5:
    print(f'Reprovado.\n média: {media}')
if media > 7:
    print(f'Aprovado.\n média: {media}')
if media > 5 and media < 6.9:
    print(f'Recuperação.\n média: {media}')