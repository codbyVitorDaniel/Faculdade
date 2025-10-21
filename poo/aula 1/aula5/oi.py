# class Motor:
#     def ligar (self):
#         print("Ligando Motor...")

# class Carro:
#     def __init__(self):
#         self.motor = Motor()
    
#     def ligar(self):
#         self.motor.ligar()

# fiatUno = Carro()
# fiatUno.ligar()
from abc import ABC ,abstractmethod


class Pagamento:
    @abstractmethod
    def pagar(self,valor):
        pass
class PagamentoPro(Pagamento):
    def pagar(self, valor):
        print(f"Pagamento de RS{valor} via promessa de pagamento")

class Pagamentocar(Pagamento):
    def pagar(self, valor):
        print(f"Pagamento de RS{valor} via cartao")
class PagamentoPix(Pagamento):
    def pagar(self, valor):
        print(f"Pagamento de RS{valor} via  pix")

def realizarpagamento(meio,valor):
    meio.pagar(valor)

realizarpagamento(PagamentoPix(),100)