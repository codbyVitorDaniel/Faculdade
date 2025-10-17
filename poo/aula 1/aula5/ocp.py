# def calcularfrete(tipo,distancia):
#     if tipo == "sedex":
#         return distancia *2.5
    
#     elif tipo == "comum":
#         return distancia *1.5
    
#     elif tipo == "sedex10":
#         return distancia *3.0
    
#     elif tipo == "drone":
#         return distancia *4.0
    
#     elif tipo == "bicicleta":
#         return distancia *1.2

from abc import ABC, abstractmethod

class FRETE(ABC):
    @abstractmethod
    def calcular(self,distancia):
        pass

class FreteComum(FRETE):
    def calcular(self, distancia):
        return distancia * 1.5
    
class FreteSedex(FRETE):
    def calcular(self, distancia):
        return distancia * 2.5
    
class FreteSedex10(FRETE):
    def calcular(self, distancia):
        return distancia * 3.5

class FretedasGalaxias(FRETE):
    def calcular(self, distancia):
        return distancia * 350

def calcularFrete(tipo: FRETE, distancia):
    return tipo.calcular(distancia)

print(f"Voce ira pagar de frete R${calcularFrete(FretedasGalaxias(),100)}")