#Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número: '))
multiplicador = 1

for multiplicador in range(1,11):
    print(f'{n} x {multiplicador} = {n*multiplicador}')
