anoAtual = int(input('Qual o ano atual? '))

for a in range(1,8):
    x = int(input(f'Qual o ano de nascimento da {a}° pessoa? '))
    idade = anoAtual - x
    if idade >= 18:
        print(f'A {a}° pessoa é maior de idade!')
    else:
        print(f'A {a}° pessoa é menor de idade.')