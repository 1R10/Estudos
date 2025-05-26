casa = int(input('Informe o valor da casa: '))
salario = int(input('Informe o valor do salário: '))
tempo = int(input('Informe o tempo, em anos, da parcela: ')) * 12

prestaçao_mensal = casa/tempo

if prestaçao_mensal > salario * 30/100:
    print('Empréstimo negado')
else: print('Empréstimo aprovado')
