#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
reais = float(input('Quantos reais você tem? '))
dolar = round(reais/5.61, 2) #14/05/2025
print(f'Você pode comprar {dolar} dólares!')
