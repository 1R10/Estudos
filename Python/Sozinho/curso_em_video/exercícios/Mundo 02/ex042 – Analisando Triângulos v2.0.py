# Precisa de correção.

ret1 = int(input('Informe um valor: '))
ret2 = int(input('Informe um valor: '))
ret3 = int(input('Informe um valor: '))
if (ret1 < ret2 + ret3) and (ret2 < ret1 + ret3) and (ret3 < ret1 and ret2):
    print('Estas retas podem formar um triângulo ')
    if ret1 == ret2 == ret3:
        print('equilátero.')
    if ret1 == ret2 or ret1 == ret3 or ret2 == ret3:
        print('isóceles')
    if ret1 != ret2 != ret3:
        print('escaleno.')
else:
    print('As retas não se tocam.')


