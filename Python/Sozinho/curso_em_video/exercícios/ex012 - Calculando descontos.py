# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input('Digite o valor do produto para a aplicação do desconto: '))
promo =  valor * 5/100
desc = valor - (promo)
print(f'Valor original: {valor}\nValor com desconto{desc}\nDesconto: {promo}')