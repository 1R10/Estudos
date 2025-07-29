anoAtual = 2025
anoNasc  = int(input('Em que ano você nasceu?'))
anoAlistamento = anoNasc + 18
if anoAlistamento < anoAtual:
    print(f'Você deveria ter se alistado em {anoAlistamento},',
          f'{(anoAlistamento - anoAtual)*-1} anos atrás.')
if anoAlistamento == anoAtual:
    print('Você tem que se alistar neste ano!')
if anoAlistamento > anoAtual:
    print(f'O ano em que você deve se alistar é em {anoAlistamento},',
          f'daqui a {anoAlistamento - anoAtual} anos.')
