from rich.traceback import install
from rich import print
install() # Importante para mostrar os erros mais detalhadamente
class funcionario():
    '''
    Esta classe atribui os dados de um funcionario (Nome, cargo e empresa)
    '''
    def __init__(self, name, job, company):
        self.nome   = name
        self.cargo  = job 
        self.empresa = company
    def __str__(self):
        return f":handshake: Prazer, meu nome é [blue]{self.nome}[/]. Trabalho como {self.cargo} na empresa {self.empresa}."
    
funcionario_um   = funcionario("Ryan", "Desenvolvedor", "Spotify")
funcionario_dois = funcionario("Rayra", "Dona", "Ryan")


print(str(funcionario_um))
print(str(funcionario_dois))
