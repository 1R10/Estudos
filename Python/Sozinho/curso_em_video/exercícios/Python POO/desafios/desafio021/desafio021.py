from rich.traceback import install
from rich import print
install()

class caneta():
    def __init__(self,cor):
        self.cores  = cor
        self.tampa  = 'on'
        self.linha  = 0
        

    def destampar(self):
        '''Destampa a caneta...'''
        self.tampa = 'off'

    def quebrar_linha(self, quantia):
        '''Quebra a linha'''
        for n in range(quantia):
            if n==0:
                print(end='')
            else:
                print('\n')

    def escrever(self,texto):
        '''Verifica se está tampada e aplica a cor.'''

        if self.tampa == 'on':
            print('Esta caneta está tampada.')
        else:
            print(f'[{self.cores}]{texto}[/]', end='')

c1 = caneta('red')
c1.escrever('vermelho')
c1.destampar()
c1.escrever('Vermelho')
c1.quebrar_linha(1)

c2 = caneta('blue')
c2.escrever('Esta é a azul.')
c2.destampar()
c2.escrever('Esta é a azul. ')
c1.escrever('Vermelha aqui.')

