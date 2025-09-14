'''
nome = input("Nome do vendendor:")
venda = float(input("Qual valor da sua venda:"))
if venda >= 500:
    print(f"O vendedor {nome} conseguiu bater a meta de 500 ele conseguiu {venda}")
else:
    faltou = venda - 500
    print(f"O vendedor {nome} nao conseguiu. Faltou {faltou} ")
'''

class loja:
    def __init__(self, nome):
        self.nome = nome
        self.venda = 0
    def vendeu(self, vendas):
        self.vendas = vendas
    def bateu(self, meta):
        if self.vendas >= meta:
            print(f'{self.nome}Bateu a meta')
        else:
            print(f'{self.nome} Nao bateu a meta')
vendedor1 = loja("Jeronimo Antonio")

vendedor1.vendeu(int(input('Digite a venda')))
vendedor1.bateu(int(input("Digite qual a meta a ser batida")))