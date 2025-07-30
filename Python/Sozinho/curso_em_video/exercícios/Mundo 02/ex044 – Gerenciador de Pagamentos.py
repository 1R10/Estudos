print('='*10, 'Lojas Moura', '='*10)

valor_compras = float(input('Preço das compras: '))
frase = f'o valor da sua compra de {valor_compras} vai custar...'
opcao = 9
while opcao != 0:
    print('      Opções de pagamento     \n',
        '[ 1 ] - A vista;\n'                ,
        '[ 2 ] - A vista no cartão;\n'      ,
        '[ 3 ] - 2x No cartão;\n'           ,
        '[ 4 ] - 3x Ou mais no cartão;\n'   ,
        '[ 5 ] - Alterar o valor;\n'        ,
        '[ 0 ] - Cancelar compra.\n'        ,
        '=================================\n')
    
    opcao = int(input('Escolha uma opção: '))

 
    if opcao == 1:
        valor_compras -= valor_compras*10/100
        print(frase,valor_compras)
        break

    if opcao == 2:
        valor_final = valor_compras - valor_compras*5/100
        print(frase, valor_final)
        break

    if opcao == 3:    
        print(f'2x de {valor_compras/2} no cartão.')
        break

    if opcao == 4:
        parcelas = int(input('Quant. de parcelas: '))
        if parcelas == 2:
            opcao = 3
        else:
            valor_final = valor_compras + parcelas * (valor_compras*30/100)
            print(frase, valor_final)
            break


    if opcao == 5:
        valor_compras = float(input('Preço das compras: '))
    if opcao == 0:
        break

# Precisa de ajustes na opção 4. Calc errado