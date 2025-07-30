import datetime
d = datetime.datetime.now()
ano = d.year

ano_nascimento = int(input('Ano de nascimento: '))
idade = ano - ano_nascimento

if idade >= 25:
    print(f'Com {idade} anos o atleta é master.')
if idade <= 14:
    print(f'Com {idade} anos o atleta é infantil.')
if idade > 14 and idade < 19:
    print(f'Com {idade} anos o atleta é júnior.')
if idade > 18 and idade < 25:    
    print(f'Com {idade} anos o atleta é sênior.')