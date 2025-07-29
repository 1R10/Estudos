valor_um   = int(input('Digite o primeiro valor:'))
valor_dois = int(input('Digite o segundo valor:'))

if valor_um > valor_dois:
    print(f'{valor_um} é maior que {valor_dois}')
if valor_um < valor_dois:
    print(f'{valor_dois} é maior que {valor_um}')
else:
    print(f'{valor_um} é igual a {valor_dois}')