from rich import print
from rich.panel import Panel
from rich.traceback import install
install()


class etiqueta():
    def __init__(self, nome, preco):
        self.produto = nome 
        self.valor   = preco
    def montar(self):
        painel = Panel(renderable=f"{self.produto}\n{20*('=')}\n{self.valor}", title="Produto", width= 25)
        print(painel)


produtoum = etiqueta(nome= "Batata", preco= "0.25")
produtoum.montar()











#Panel(renderable=f"selfproduto\n{20*('=')}\nselfvalor", title="Produto", width= 25)