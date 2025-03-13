tupla = ('zero','um','dois','três','quatro','cinco',
         'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze','treze', 'cartoze', 'quinte', 'dezesseis',
         'dezessete', 'dezoito''dezenove', 'vinte')

valor = int(input('Qual valor, entre zero e vinte, você deseja ver por extenso? '))
while valor >20 or valor < 0:
    print('\nValor inválido. Escolha entre zero e vinte.')
    valor = int(input('\nQual valor, entre zero e vinte, você deseja ver por extenso? '))

print(f'\n{valor} por extenso é "{tupla[valor]}"')