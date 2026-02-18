class Conta_Bancaria:
    '''
    Cria uma conta bancária e permite fazer saques/depósitos
    '''
    #Continuar de 29:00
    def __init__(self, id, nome, saldo = 0):
        self.id      = id
        self.titular = nome
        self.saldo   = saldo
    def __str__(self):
        return f"A conta {self.id}, do titular {self.titular}, possui um saldo de R${self.saldo:.2f}"

# Área do uso da classe # ------------------------------------------------------------------------------------------
conta_um = Conta_Bancaria(id = 1, nome = "Ryan", saldo = 0.73)
print(conta_um)