import time
v1 = 'n'
while True:
    if v1 == 'n':
        v1 = int(input('Digite um valor: '))
        v2 = int(input('Digite um valor: '))
    else:
    
        print('\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5]Sair do programa')

        escolha = int(input('\nO que você deseja fazer?'))

        if   escolha == 1: print(f'\n{v1} + {v2} = {v1+v2}')
        elif escolha == 2: print(f'\n{v1} X {v2} = {v1*v2}')
        elif escolha == 3:
            if   v1 > v2: print(f'{v1} > {v2}')
            elif v1 < v2: print(f'{v2} > {v1}')
        elif escolha == 4:
            v1 = int(input('Digite um valor: '))
            v2 = int(input('Digite um valor: '))
        elif escolha == 5: break
print('Fim do programa!')