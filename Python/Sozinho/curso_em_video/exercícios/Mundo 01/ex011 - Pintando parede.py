# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
larg = float(input('Digite a largura da parede: '))
altu = float(input('Digite a altura da parede: ' ))
area = altu*larg

tinta = area/2
print(f'Para pintar uma parede de {area} metros², será necessário utilizar {tinta} baldes de tinta.')
