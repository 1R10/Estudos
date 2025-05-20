nome = str(input('Digite o seu nome completo: ')).strip()

moura_Nome = 'MOURA' in nome.upper()
if 'MOURA' in nome.upper():
    print('Seu nome tem Moura.')
else: print('Seu nome não tem Moura.')