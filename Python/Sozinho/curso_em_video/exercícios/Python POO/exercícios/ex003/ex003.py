class Conta_Bancaria:
    '''
    Cria uma conta bancária e permite fazer saques/depósitos
    '''

# Definição de classe # ---------------------------------------------------------------------------------------------

    def __init__(self, id, nome, saldo = 0):
        self.id      = id
        self.titular = nome
        self.saldo   = saldo
        print(f"Conta {self.id} Criada com sucesso!\nTitular:{self.titular}\nSaldo: {self.saldo:.2f}")
   
    def __str__(self):
        return f"A conta {self.id}, do titular {self.titular}, possui um saldo de R${self.saldo:.2f}"
    
# Saque/Depósito # ---------------------------------------------------------------------------------------------------
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} AUTORIZADO.\nNovo saldo: R${self.saldo}")
        else:
            print(f"Saque de R${valor:.2f} NEGADO.")
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} AUTORIZADO.\nNovo saldo: R${self.saldo}")
        else: 
            print(f"Saque de R${valor:.2f} NEGADO por saldo insuficiente.")
        
# Área do uso da classe # ------------------------------------------------------------------------------------------
conta_um = Conta_Bancaria(id = 1, nome = "Ryan", saldo = 0.73)