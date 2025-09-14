class Banco:
    def __init__(self):
        self.saldo = 0
    def depositar(self,valor):
        self.saldo += valor
        print("Saldo:",self.saldo)

conta = Banco()
conta.depositar(100)



