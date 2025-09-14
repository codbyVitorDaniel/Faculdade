# do que vai depositar
# aonde vai depositar
# quanto vai despositar
class Banco:
    conta1 = 0
    conta2 = 0
    conta3 = 0
    def __init__(self, saldo):
        self.saldo = saldo
    def perguntas(self):
        print(f"Seu saldo e esse:{self.saldo}")
        movi = float(input("Digite 1- retirada ou 2- deposito?\n"))
        if movi == 2 :
            escolha = int(input("Para qual conta?\n"))
            if escolha == 1:
                quanto = int(input("Quanto vc quer depositar?"))
                Banco.conta1 = quanto + self.saldo
                print(f"Seu saldo e {self.saldo}")
            elif escolha == 2:
                quanto = int(input("Quanto vc quer depositar?"))
                Banco.conta2 = quanto + self.saldo
                print(f"Seu saldo e {self.saldo}")
            elif escolha == 3:
                quanto = int(input("Quanto vc quer depositar?"))
                Banco.conta3 = quanto + self.saldo
                print(f"Seu saldo e {self.saldo}")
            else:
                print("Error")
        elif movi == 1:
            conta = int(input("Qual conta vc quer retirar:"))
            if conta == 1:
                Banco.conta1 = Banco.conta1 - conta
                print(f"O valor da sua conta e {Banco.conta1}")
            elif conta == 2:
                Banco.conta2 = Banco.conta2 - conta
                print(f"Seu saldo e {Banco.conta3}")
            elif conta == 3:
                Banco.conta3 = Banco.conta3 - conta
                print(f"Seu saldo e {Banco.conta3}")
    def contas (self):
        print("Vc")
ba = Banco(1000)
cal = ba.perguntas()