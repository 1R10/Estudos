from rich.traceback import install
from rich import print
from time import sleep
install()

class livro():
    def __init__(self, titulo, paginas):
        self.nome    = titulo
        self.tamanho = paginas

    def avancar_paginas(self, avancar: int):
        '''Esta def é para avançar páginas'''
        pagina_atual = self.tamanho+1 - self.tamanho
        print(f'Você acabou de abrir o livro [red]{self.nome}[/]. Ele possuo um total de {self.tamanho} páginas.\n Você está na [red]página {pagina_atual}[/]')
        print(f'Você vai avançar {avancar} páginas')
        while avancar != 0:
            if pagina_atual < self.tamanho:
                sleep(0.5)
                avancar -= 1
                pagina_atual += 1         
                print(f'--> Pag{pagina_atual}',end='')
                if avancar == 0:
                    print(f'\nVocê chegou na página {pagina_atual}')
            if pagina_atual == self.tamanho:
                print('Não é possível avançar mais. Você chegou no fim do livro.')
                break

            
            
l1 =livro("Motivos para amar", 432)
l1.avancar_paginas(12)

        

        



