cidade = input('Qual o nome da sua cidade?\n').upper().strip()
santiCidade = (cidade[:5] == 'SANTO')
if santiCidade:
    print(f'Sua cidade, {cidade}, começa com "Santo".')
else:
    print(f'Sua cidade, {cidade}, não começa com "Santo".')
