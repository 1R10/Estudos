from rich.traceback import install
from rich.panel import Panel
from rich import print
install()

class gamer():
    def __init__(self,nick,name):
        self.nickname = nick 
        self.realname = name
        self.favgames = []
    
    def add_Fav(self, jogo):
        '''Adiciona jogos favoritos para uma ficha.'''
        self.favgames += ['[green]-->[/] ' + jogo]
        
    def ficha(self):
        '''Vai mostrar os dados de uma conta. nome,nick e jogos favs'''

        dados = f'[blue]Nome:[/] {self.realname}\n[blue]Nick: [/]{self.nickname}'
        jogos = '\n'.join(self.favgames)
        fichinha = Panel(renderable=(dados + '\n[blue]Jogos favoritos:[/] \n' + jogos), title='Jogador ' + self.nickname, width= 50)

        print(fichinha)




j1 = gamer('_XxDestruidor8000xX_','Enzo Valetino')
j1.add_Fav('Mewgenics')
j1.add_Fav('Minecraft')
j1.add_Fav('Hades')
j1.ficha()