import clima, encontraCEP

menu = '''
[1] --> Inserir CEP
[2] --> Ver dados do CEP
[3] --> Ver temperatura
[0] --> Encerrar
'''
    
while True:
    print(menu)
    try:
        escolha_menu = int(input('Escolha uma opção: '))
        if escolha_menu == 0:
            break
        if escolha_menu == 1:
            cep = int(input('Insira seu CEP'))
            encontraCEP.formatarCEP(cep)
        if escolha_menu == 2:
            print('Esta área está em construção. Tente outra opção!')
        if escolha_menu == 3:
            print('Esta área está em construção. Tente outra opção!')
    except:
        print('erro cuzao')
        