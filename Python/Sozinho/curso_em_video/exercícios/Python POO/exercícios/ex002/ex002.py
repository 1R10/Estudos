# Classe
class Gafanhoto:
    '''
    Esta classe vai mostrar os dados de um gafanhoto
    '''
    def __init__(self, n = "não_atribuído", i = 0): # Método construtor
        # Atributos de instância
        self.nome = n
        self.idade = i
        
        # Métodos de instância
    def aniversario(self):
        self.idade += 1
    
    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    
    def __getstate__(self):
        return f"Estado: nome = {self.nome}; Idade = {self.idade}"  

# Objeto
g1 = Gafanhoto('Ryan', 22)
print(g1.__getstate__())
g2 = Gafanhoto('Rayra', 23)
g2.aniversario() # idade + 1
print(g2)
