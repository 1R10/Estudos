n = int(input('Digite um número de até 4 dígitos: '))
if 0 < n < 9999:
    milhar = n//1000
    n = n - milhar*1000

    centena = n//100
    n = n - centena*100

    dezena = n//10
    n = n - dezena*10

    print(f'Milhar: {milhar}\nCentena: {centena}\nDezena: {dezena}\nUnidade: {n}')
else:
    print(f'{n} possui mais de 4 dígitos')
