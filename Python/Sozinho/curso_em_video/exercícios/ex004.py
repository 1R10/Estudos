# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele

valor = input('\nDigite algo: ')
tipo  = type(valor)

print(f'{valor} é numérico?.....{valor.isnumeric()}')
print(f'{valor} é alfabético?...{valor.isalpha()}')
print(f'{valor} é decimal?......{valor.isdecimal()}')
print(f'{valor} é minúsculo?....{valor.islower()}')
print(f'{valor} é só espaços?...{valor.isspace()}')
print(f'{valor} é maiúsculo?....{valor.isupper()}')
'''
isnumeric()
isalpha()
isdecimal()
islower()
isspace()
isupper()
'''

