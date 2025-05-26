carro = int(input('Qual a velocidade do carro?\n'))
if carro > 80:
    multa = (carro - 80) * 7
    print(f'Você ultrapassou o limite de velocidade. A multa será de R${multa},00')
else: print('Tá liberado')
