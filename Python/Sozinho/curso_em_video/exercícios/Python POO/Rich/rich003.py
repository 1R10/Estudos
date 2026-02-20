from rich.table import Table
from rich import print

tabela = Table(title= "Tabela de preços")

tabela.add_column("Item", justify= "center", style= "red")
tabela.add_column("Preço")

tabela.add_row("Lápis", "R$0.50")
tabela.add_row("Caneta", "R$1.50")
print(tabela)