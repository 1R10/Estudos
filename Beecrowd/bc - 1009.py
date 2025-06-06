nome          = input('')
salario_fixo  = float(input(''))
vendas_totais = float(input(''))

comissao15 = vendas_totais *(15/100)
salario_total = salario_fixo + comissao15
print(f'TOTAL = R$ {salario_total:.2f}')