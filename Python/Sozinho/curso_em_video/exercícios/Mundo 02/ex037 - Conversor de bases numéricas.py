numero_Inteiro = int(input('Digite um número inteiro: '))
opcao = 1
print('Agora vamos decidir se ele vai ser convertido para binário, hexadecimal ou octal.\n')
while opcao != 0:
    print('     OPÇÕES')
    print('[ 0 ] - Encerrar')
    print('[ 1 ] - Binário')
    print('[ 2 ] - Hexadecimal')
    print('[ 3 ] - Octal')
    print('[ 4 ] - Todas as conversões')
    print('[ 5 ] - Novo número')

    opcao = int(input('Escolha sua opção: '))
    print('\n'*4)
    binario = bin(opcao)
    hexadec = hex(opcao)
    octal   = oct(opcao)

    if opcao > 0 and opcao < 6:
        if opcao == 1:print(f'Binário: {binario}', '\n'*4)
        if opcao == 2:print(f'Hexadecimal: {hexadec}', '\n'*4)
        if opcao == 3:print(f'Octal: {octal}', '\n'*4)
        if opcao == 4:print(f'Binário: {binario}\nHexadecimal: {hexadec}\nOctal: {octal}', '\n'*4)
        if opcao == 5:
            numero_Inteiro = int(input('Digite um número inteiro'))
    else: break
print('Fim do programa!')