# Classe
class Gafanhoto:
    def __init__(self): # Método construtor
        # Atributos de instância
        self.nome = "Ryan" #input('Qual o seu nome?\n')
        self.idade = int(input('Qual a sua idade?\n'))
        
        # Métodos de instância
    def aniversario(self):
        self.idade += 1
    
    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

g1 = Gafanhoto()
print(g1.mensagem())

# Objeto

# Parei a aula em 26:16