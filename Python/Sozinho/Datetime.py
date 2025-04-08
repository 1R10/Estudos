import datetime 

# Localiza data e a hora atual
d = datetime.datetime.now()

# Separação por dias, mês e ano
dia = d.day
mes = d.month
ano = d.year
nome_do_dia = d.strftime('%A') # Em inglês
nome_do_mes = d.strftime('%B') # Em inglês

# Mostra na tela em formato dd/mm/aaaa
print(f'\nO dia de hoje é {dia}/{mes}/{ano}\n')
