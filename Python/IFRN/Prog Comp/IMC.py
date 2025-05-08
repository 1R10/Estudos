print('Bem vindo ao calculador de IMC!')
peso = float(input('Informe o peso em kg: '))
altura = float(input('Informe sua altura em cm: '))
altura = altura / 100

imc = round(peso / (altura**2),1)

if imc <= 18.5:
    classificacao = 'magreza'
    grau = 0
    #print('Com o IMC de', imc, ', você está na magreza.')
if 18.5 < imc <= 24.9:
    classificacao = 'normal'
    grau = 0
    #print('Com o IMC de', imc, ', você está na normalidade.')
if 25 < imc <= 29.9:
    classificacao = 'sobrepeso'
    grau = 1
    #print('Com o IMC de', imc, ', você está no sobrepeso e na obesidade grau 1.')
if 30 < imc <= 39.9:
    classificacao = 'obesidade'
    grau = 2
    #print('Com o IMC de', imc, ', você está na obesidade e no grau 2.')
if imc > 40:
    classificacao = 'obesidade grave'
    grau = 3
    #print('Com o IMC de', imc, ', você está na obesidade grave e no grau 3.')

print('IMC: ',imc)
print('Classificação: ', classificacao)
print('Grau: ',grau)
