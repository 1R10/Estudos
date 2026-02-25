from rich import print
from rich.panel import Panel
from rich.traceback import install
install()


class etiqueta():
    def __init__(self, nome, preco):
        self.produto = nome 
        self.valor   = preco
    def __rich__(self):
        painel = Panel(renderable=f"{self.produto}\n{20*('=')}\n{self.valor}", title="Produto", width= 25)
        return painel


produtoum = etiqueta(nome= "Batata", preco= "0.25")
print(produtoum)











#Panel(renderable=f"selfproduto\n{20*('=')}\nselfvalor", title="Produto", width= 25)