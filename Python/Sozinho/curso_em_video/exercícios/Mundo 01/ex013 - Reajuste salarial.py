# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o salário atual: '))
aumento = salario * 15/100
salario_novo = salario + aumento

print(f'Salário velho: {salario}\nAumento: {aumento}\nSalário novo: {salario_novo}')