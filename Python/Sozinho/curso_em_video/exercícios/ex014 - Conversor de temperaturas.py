# Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celso = int(input('Digite a temperatuda em C°: '))
fahre = round(celso * 1.8 + 32,2)
print(f'Celsius: {celso}°\nFahreinheint: {fahre}°')