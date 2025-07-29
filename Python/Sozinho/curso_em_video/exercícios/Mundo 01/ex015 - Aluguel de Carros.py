#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
# a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km_percorrido = float(input('Qual a quantidade de Km percorridos na viagem?\n'))
tempo_alugado = int(input('Por quantos dias o carro foi alugado?\n'))

gasolina = km_percorrido * 0.15
aluguel  = tempo_alugado * 60
valor_total = round(aluguel + gasolina,2)
print(f'Aluguel: {aluguel}\nGasolina: {gasolina}\nValor pra pagar: {valor_total}')

#ou
#valor_total = km_percorrido * 0.15 + tempo_alugado * 60