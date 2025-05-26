ret1 = int(input('Informe um valor: '))
ret2 = int(input('Informe um valor: '))
ret3 = int(input('Informe um valor: '))

if ret1 < ret2 + ret3 and ret2 < ret1 + ret3 and ret3 < ret1 and ret2:
    print('As retas se tocam.')
else: print('Não se tocam.')
