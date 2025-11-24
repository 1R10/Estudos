import clima, encontraCEP

menu = '''
[1] --> Inserir CEP
[0] --> Encerrar
'''
    
while True:
    print(menu)
    try:
        escolha_menu = int(input('Escolha uma opção: '))
        if escolha_menu == 0:
            print('Encerrando...')
            break
        if escolha_menu == 1:
            cep = int(input('Insira seu CEP'))
            if encontraCEP.limpaCEP(cep):
                encontraCEP.mostra_cep()
            else:
                print('Ocorreu um erro')
    except:
        print('Ocorreu um erro. Tente novamente')
        