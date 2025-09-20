class bemVindo:
    def __init__(self,nome , idade):
        self.nome = nome
        self.idade = idade
    def saudaçao(self):
        print(f"Seja bem vindo {self.nome} sua idade e {self.idade}")

bem = bemVindo("vitor",  10)
bem.saudaçao()
