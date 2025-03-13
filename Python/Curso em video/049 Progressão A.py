a1 = int(input('Primeiro termo da PA:'))
razao = int(input('Razão da PA:'))
an = a1 + (10 - 1) * razao
for n in range(1, 11):  
    print(f'{a1} -> ', end='')
    a1 += razao