while True:
    sex = input('\nQual o seu sexo? ')
    if sex == 'm':
        print('Vc é homem')
    elif sex == 'nb':
        print('Tu é nékk')
    elif sex == 'f':
        print('Vc é uma madame')
    else:
        print('Digite m,f ou nb!')
    laço = input('Continuar?(s/n)').lower()
    if laço != 's':break
print('Fim do código!')