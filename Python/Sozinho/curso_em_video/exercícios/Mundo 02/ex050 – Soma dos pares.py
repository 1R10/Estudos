soma = 0
l_numeros = []
for n in range(1,7):
    numero = int(input(f'Digite o valor {n}: '))
    if numero%2==0:
        soma += numero
        
        l_numeros.append(numero)

print(f'A soma de {l_numeros} é igual a {soma}')