#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros      = int(input('Insira uma medida em metros: '))
centimetros = metros * 100
milímetros  = metros * 1000

print(f'Valor em metro: {metros}')
print(f'Valor em centímetro: {centimetros}')
print(f'Valor em milímetro: {milímetros}')
