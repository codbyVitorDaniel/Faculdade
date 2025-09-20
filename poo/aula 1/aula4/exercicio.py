class Modificador:
    @staticmethod
    def Maiusculo(valor):
        return valor.upper()

    @staticmethod
    def minusculo(valor):
        return valor.lower()

    @staticmethod
    def capitalizar(valor):
        return valor.capitalize()

    @staticmethod
    def remover_espacos(valor):
        return valor.strip()

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = float(preco)

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        if isinstance(novo_preco, (int, float)) and novo_preco >= 0:
            self._preco = float(novo_preco)
        else:
            print("Preço inválido. Deve ser um número positivo.")

nome_produto_original = "  camiseta azul "


nome_modificado = Modificador.capitalizar(Modificador.remover_espacos(nome_produto_original))

produto1 = Produto(nome_modificado, 100)
produto1.preco = -99  

print(f"{produto1.nome} -> R$ {produto1.preco:.2f}")
