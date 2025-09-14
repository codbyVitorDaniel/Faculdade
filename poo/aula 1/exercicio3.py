class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir(self):
        print(f'Marca:{self.marca} modelo:{self.modelo} Ano:{self.ano}')

pergunta1 = input('Modelo de Caroo')
pergunta2 = input('Marca do carro')
pergunta3 = int(input('Ano do carro'))

carro1 = Carro(pergunta1 , pergunta2, pergunta3)
carro1.exibir()


'''
carro1 = Carro('Toyota', 'Corola',2010)
carro1.exibir()
carro2 = Carro('Volkswagem', 'Gol', 2010)
carro2.exibir()
carro3 = Carro('BYD', 'Dolphin', 2024)
carro3.exibir()
'''