numero = int(input('Digite um número: '))
multiplicador = int(input('Limite da tabuada: '))
for n in range(1,multiplicador+1):
    print(f'{numero} x {n} = {n*numero}')