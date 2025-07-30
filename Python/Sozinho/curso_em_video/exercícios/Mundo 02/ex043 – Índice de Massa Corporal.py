peso   = int(input('Peso em KG: '))
altura = int(input('Altura em cm: '))
imc = peso/altura**2

frase = f'Seu IMC é {imc}. Você se classifica em'

if imc < 18.5:
    print(f'{frase} abaixo do peso.')
if 18.5 <= imc <= 25:
    print(f'{frase} peso ideal.')
if 25 < imc <= 30:
    print(f'{frase} sobrepeso.')
if 30 < imc <= 40:
    print(f'{frase} obesidade.')
if imc > 40:
    print(f'{frase} obesidade morbida.')