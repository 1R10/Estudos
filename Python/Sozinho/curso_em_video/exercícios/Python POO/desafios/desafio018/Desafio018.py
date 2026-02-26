from rich.traceback import install
from rich.panel import Panel
from rich import print
# 400g de carne por pessoa
# 82,40kg

install()
class churrasco():
    '''
    Esta classe vai analisar o valor de repartição para cada pessoa em um churrasco
    '''
    def __init__(self,titulo, pessoas=0):
        self.nome    = titulo
        self.quantia = pessoas

    
    def analisar(self):
        analise = Panel(renderable=f"Analisando [green]{self.nome}[/] com [blue]{self.quantia}[/] pessoas...\n" +
                        "Cada participante comerá 0.4kg de carne e cada Kg custa R$82,40\n" +
                        f"O custo total será de [green]R${(self.quantia*0.4)*82.40:.2f}[/]\n"+
                        f"Ficando [green]R${((self.quantia*0.4)*82.40)/self.quantia:.2f}[/] para cada participante",
                         
                          title= f"{self.nome}" ,style="white", width= 100)
        print(analise)
        

c1 = churrasco("Churras", pessoas=100)

c1.analisar()

