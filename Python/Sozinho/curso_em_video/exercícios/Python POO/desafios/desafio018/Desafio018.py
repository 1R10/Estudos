from rich.traceback import install
from rich.panel import Panel
from rich import print
# 400g de carne por pessoa
# 82,40kg

install()
class churrasco():
    def __init__(self,titulo, pessoas=0):
        self.nome    = titulo
        self.quantia = pessoas


    def analisar(self):
        analise = Panel(renderable=f"Analisando [green]{self.nome}[/] com [blue]{self.quantia}[/] pessoas", title= f"{self.nome}" ,style="white", width= 50)
        print(analise)
        

c1 = churrasco("Churras", pessoas=15)

c1.analisar()

