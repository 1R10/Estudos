salario = int(input('Informe um valor: '))
if salario <= 1250:
    aumento = salario * (10/100)
    salario += aumento

else:
        aumento = salario * (15/100)
        salario += aumento
print(f'O aumento foi de {aumento}. O salário novo é de {salario}')
