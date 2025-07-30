#em andamento
from random import randint
print('=' * 50,'\n'                                      ,
      'Bem vindo ao jogo de pedra, papel e tesoura!\n'   ,
      '=' * 50,'\n'                                      ,
      'Você pode escolher as seguintes opções:\n'        ,
      '[1] Pedra\n'                                      , 
      '[2] Papel\n'                                      ,
      '[3] Tesoura'                                       )
opcao = int(input('Com base no número, escolha a sua opção:')) - 1  # Adjust for zero-based index


itens = ['Pedra', 'Papel', 'Tesoura']


jogador = itens[opcao]
computador = itens[randint(1, 3)]
	
print(f'Jogador escolheu: {jogador}')
print(f'Computador escolheu: {computador}')