# """
# ================================================================================
# PROVA P2 - PROGRAMAÇÃO ORIENTADA A OBJETOS
# Professor: Tiago Castro
# Turma: 4º Período - Engenharia de Software
# Universidade de Vassouras
# ================================================================================

# QUESTÃO 2: PRINCÍPIO SOLID - INTERFACE SEGREGATION PRINCIPLE (ISP)
# VALOR: 3 pontos (se respeitado o princípio corretamente)

# TEMA: SISTEMA DE VEÍCULOS

# Esta questão aborda o Princípio de Segregação de Interface aplicado a um
# sistema de gerenciamento de diferentes tipos de veículos. Você deve refatorar
# o código abaixo aplicando o ISP.

# ================================================================================

# O Princípio de Segregação de Interface estabelece que os clientes não devem
# ser forçados a depender de interfaces que não utilizam. É melhor ter várias
# interfaces específicas do que uma interface geral "gorda".

# ================================================================================
# """

# # ============================================================================
# # EXEMPLO QUE NÃO RESPEITA O ISP
# # ============================================================================
# # 
# # A interface Veiculo abaixo viola o ISP porque:
# # - Força todas as classes que a implementam a ter métodos que podem não
# #   fazer sentido para elas
# # - Um Carro precisa ligar, acelerar, frear e abastecer (faz sentido)
# # - Uma Bicicleta precisa ligar, acelerar e frear, mas NÃO precisa abastecer
# #   (mas é forçada a implementar esse método!)
# # - Um Barco precisa ligar, acelerar, frear e abastecer, mas NÃO precisa
# #   trocar_pneu (mas é forçada a implementar esse método!)
# #
# # PROBLEMA: Classes são forçadas a implementar métodos que não fazem sentido
# # para elas, resultando em implementações vazias ou que lançam exceções.
# #
# # ============================================================================

# from abc import ABC, abstractmethod

# class Veiculo(ABC):
#     """
#     PROBLEMA: Interface "gorda" que força implementação de métodos
#     que podem não fazer sentido para todas as classes.
#     """
#     @abstractmethod
#     def ligar(self):
#         """Liga o veículo"""
#         pass
    
#     @abstractmethod
#     def acelerar(self, velocidade):
#         """Acelera o veículo"""
#         pass
    
#     @abstractmethod
#     def frear(self):
#         """Freia o veículo"""
#         pass
    
#     @abstractmethod
#     def abastecer(self, quantidade):
#         """Abastece o veículo com combustível"""
#         pass
    
#     @abstractmethod
#     def trocar_pneu(self, posicao):
#         """Troca o pneu do veículo"""
#         pass


# class Carro(Veiculo):
#     """Carro implementa todos os métodos (faz sentido)"""
#     def __init__(self, modelo, combustivel=0):
#         self.modelo = modelo
#         self.combustivel = combustivel
#         self.ligado = False
#         self.velocidade = 0
    
#     def ligar(self):
#         if self.combustivel > 0:
#             self.ligado = True
#             return f"{self.modelo} ligado!"
#         return f"{self.modelo} sem combustível!"
    
#     def acelerar(self, velocidade):
#         if not self.ligado:
#             return f"{self.modelo} precisa estar ligado!"
#         self.velocidade += velocidade
#         return f"{self.modelo} acelerando para {self.velocidade} km/h"
    
#     def frear(self):
#         if self.velocidade > 0:
#             self.velocidade = max(0, self.velocidade - 20)
#             return f"{self.modelo} freando. Velocidade: {self.velocidade} km/h"
#         return f"{self.modelo} já está parado"
    
#     def abastecer(self, quantidade):
#         self.combustivel += quantidade
#         return f"{self.modelo} abastecido com {quantidade}L. Total: {self.combustivel}L"
    
#     def trocar_pneu(self, posicao):
#         return f"Pneu {posicao} do {self.modelo} trocado com sucesso!"


# class Bicicleta(Veiculo):
#     """
#     PROBLEMA: Bicicleta é forçada a implementar abastecer() e trocar_pneu()
#     mesmo que não faça sentido! Isso viola o ISP.
#     """
#     def __init__(self, modelo):
#         self.modelo = modelo
#         self.ligado = False
#         self.velocidade = 0
    
#     def ligar(self):
#         # Bicicleta não precisa "ligar", mas é forçada a implementar
#         self.ligado = True
#         return f"{self.modelo} pronta para uso!"
    
#     def acelerar(self, velocidade):
#         if not self.ligado:
#             return f"{self.modelo} precisa estar pronta!"
#         self.velocidade += velocidade
#         return f"{self.modelo} pedalando a {self.velocidade} km/h"
    
#     def frear(self):
#         if self.velocidade > 0:
#             self.velocidade = max(0, self.velocidade - 15)
#             return f"{self.modelo} freando. Velocidade: {self.velocidade} km/h"
#         return f"{self.modelo} já está parada"
    
#     def abastecer(self, quantidade):
#         # PROBLEMA: Bicicleta não abastece! Implementação vazia ou exceção
#         raise NotImplementedError("Bicicletas não precisam de combustível!")
    
#     def trocar_pneu(self, posicao):
#         # PROBLEMA: Bicicleta tem pneus, mas a lógica é diferente!
#         # Implementação forçada que pode não fazer sentido
#         return f"Pneu {posicao} da {self.modelo} trocado (mas não é como carro!)"


# class Barco(Veiculo):
#     """
#     PROBLEMA: Barco é forçado a implementar trocar_pneu() mesmo que
#     não faça sentido! Isso viola o ISP.
#     """
#     def __init__(self, modelo, combustivel=0):
#         self.modelo = modelo
#         self.combustivel = combustivel
#         self.ligado = False
#         self.velocidade = 0
    
#     def ligar(self):
#         if self.combustivel > 0:
#             self.ligado = True
#             return f"{self.modelo} ligado!"
#         return f"{self.modelo} sem combustível!"
    
#     def acelerar(self, velocidade):
#         if not self.ligado:
#             return f"{self.modelo} precisa estar ligado!"
#         self.velocidade += velocidade
#         return f"{self.modelo} navegando a {self.velocidade} nós"
    
#     def frear(self):
#         if self.velocidade > 0:
#             self.velocidade = max(0, self.velocidade - 10)
#             return f"{self.modelo} reduzindo velocidade. Velocidade: {self.velocidade} nós"
#         return f"{self.modelo} já está parado"
    
#     def abastecer(self, quantidade):
#         self.combustivel += quantidade
#         return f"{self.modelo} abastecido com {quantidade}L. Total: {self.combustivel}L"
    
#     def trocar_pneu(self, posicao):
#         # PROBLEMA: Barco não tem pneus! Implementação vazia ou exceção
#         raise NotImplementedError("Barcos não têm pneus!")


# Exemplo de uso (problema):
# carro = Carro("Fusca")
# carro.ligar()  # OK
# carro.abastecer(50)  # OK
# carro.trocar_pneu("dianteiro")  # OK
# 
# bicicleta = Bicicleta("Caloi")
# bicicleta.ligar()  # OK
# bicicleta.abastecer(10)  # ERRO! Não faz sentido
# 
# barco = Barco("Lancha")
# barco.ligar()  # OK
# barco.trocar_pneu("dianteiro")  # ERRO! Não faz sentido


# ============================================================================
# ÁREA PARA SUA IMPLEMENTAÇÃO
# ============================================================================

# TODO: Implemente aqui sua solução aplicando o ISP



# Implemente aqui o exemplo de uso:


from abc import ABC, abstractmethod



class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass


class Aceleravel(ABC):
    @abstractmethod
    def acelerar(self, velocidade):
        pass


class Freavel(ABC):
    @abstractmethod
    def frear(self):
        pass


class Abastecivel(ABC):
    @abstractmethod
    def abastecer(self, quantidade):
        pass


class ComPneu(ABC):
    @abstractmethod
    def trocar_pneu(self, posicao):
        pass



class Carro(Ligavel, Aceleravel, Freavel, Abastecivel, ComPneu):
    def __init__(self, modelo, combustivel=0):
        self.modelo = modelo
        self.combustivel = combustivel
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if self.combustivel > 0:
            self.ligado = True
            return f"{self.modelo} ligado!"
        return f"{self.modelo} sem combustível!"

    def acelerar(self, velocidade):
        if not self.ligado:
            return f"{self.modelo} precisa estar ligado!"
        self.velocidade += velocidade
        return f"{self.modelo} acelerando para {self.velocidade} km/h"

    def frear(self):
        if self.velocidade > 0:
            self.velocidade = max(0, self.velocidade - 20)
            return f"{self.modelo} freando. Velocidade: {self.velocidade} km/h"
        return f"{self.modelo} já está parado"

    def abastecer(self, quantidade):
        self.combustivel += quantidade
        return f"{self.modelo} abastecido com {quantidade}L. Total: {self.combustivel}L"

    def trocar_pneu(self, posicao):
        return f"Pneu {posicao} do {self.modelo} trocado com sucesso!"


class Bicicleta(Ligavel, Aceleravel, Freavel, ComPneu):
    """Bicicleta não abastece! Então não implementa Abastecivel."""
    def __init__(self, modelo):
        self.modelo = modelo
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        self.ligado = True
        return f"{self.modelo} pronta para uso!"

    def acelerar(self, velocidade):
        if not self.ligado:
            return f"{self.modelo} precisa estar pronta!"
        self.velocidade += velocidade
        return f"{self.modelo} pedalando a {self.velocidade} km/h"

    def frear(self):
        if self.velocidade > 0:
            self.velocidade = max(0, self.velocidade - 15)
            return f"{self.modelo} freando. Velocidade: {self.velocidade} km/h"
        return f"{self.modelo} já está parada"

    def trocar_pneu(self, posicao):
        return f"Pneu {posicao} da {self.modelo} trocado!"


class Barco(Ligavel, Aceleravel, Freavel, Abastecivel):
    """Barco não tem pneus! Então não implementa ComPneu."""
    def __init__(self, modelo, combustivel=0):
        self.modelo = modelo
        self.combustivel = combustivel
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if self.combustivel > 0:
            self.ligado = True
            return f"{self.modelo} ligado!"
        return f"{self.modelo} sem combustível!"

    def acelerar(self, velocidade):
        if not self.ligado:
            return f"{self.modelo} precisa estar ligado!"
        self.velocidade += velocidade
        return f"{self.modelo} navegando a {self.velocidade} nós"

    def frear(self):
        if self.velocidade > 0:
            self.velocidade = max(0, self.velocidade - 10)
            return f"{self.modelo} reduzindo velocidade. Velocidade: {self.velocidade} nós"
        return f"{self.modelo} já está parado"

    def abastecer(self, quantidade):
        self.combustivel += quantidade
        return f"{self.modelo} abastecido com {quantidade}L. Total: {self.combustivel}L"


# ================================================================
# EXEMPLO DE USO
# ================================================================

if __name__ == "__main__":
    carro = Carro("Fusca", combustivel=20)
    bicicleta = Bicicleta("Caloi")
    barco = Barco("Lancha", combustivel=60)

    print(carro.ligar())
    print(carro.trocar_pneu("dianteiro"))
    print()

    print(bicicleta.ligar())
    print(bicicleta.acelerar(1000000))
    print()

    print(barco.ligar())
    print(barco.abastecer(1500000))

