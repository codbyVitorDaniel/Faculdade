"""
================================================================================
GABARITO - SIMULADO P2 - PROGRAMAÇÃO ORIENTADA A OBJETOS
Professor: Tiago Castro
Turma: 4º Período B - Engenharia de Software
================================================================================

PRINCÍPIO: OPEN/CLOSED PRINCIPLE (OCP)
VALOR: 1,0 ponto

SOLUÇÃO CORRETA
================================================================================
"""

from abc import ABC, abstractmethod

# ============================================================================
# SOLUÇÃO APLICANDO O OCP
# ============================================================================
# 
# Agora podemos adicionar novos tipos de desconto SEM MODIFICAR
# a CalculadoraDesconto. Apenas criamos uma nova classe que implementa
# a estratégia de desconto.
#
# ============================================================================

class DescontoStrategy(ABC):
    """
    Interface abstrata que define o contrato para estratégias de desconto.
    Qualquer novo tipo de desconto só precisa implementar esta interface.
    """
    @abstractmethod
    def calcular_desconto(self, valor):
        """Calcula o desconto baseado no valor"""
        pass


class DescontoVIP(DescontoStrategy):
    """Estratégia de desconto para clientes VIP (20%)"""
    def calcular_desconto(self, valor):
        return valor * 0.20


class DescontoPremium(DescontoStrategy):
    """Estratégia de desconto para clientes Premium (15%)"""
    def calcular_desconto(self, valor):
        return valor * 0.15


class DescontoRegular(DescontoStrategy):
    """Estratégia de desconto para clientes Regulares (5%)"""
    def calcular_desconto(self, valor):
        return valor * 0.05


class CalculadoraDesconto:
    """
    Agora a calculadora recebe uma estratégia de desconto ao invés de
    um tipo de cliente. Está FECHADA para modificação, mas ABERTA para extensão.
    """
    def __init__(self, estrategia: DescontoStrategy):
        self.estrategia = estrategia
    
    def calcular_desconto(self, valor):
        """
        Delega o cálculo do desconto para a estratégia injetada.
        Não precisa mais de if/elif para cada tipo!
        """
        return self.estrategia.calcular_desconto(valor)


# ============================================================================
# EXEMPLO DE USO
# ============================================================================

if __name__ == "__main__":
    # Usar com desconto VIP
    calc_vip = CalculadoraDesconto(DescontoVIP())
    desconto_vip = calc_vip.calcular_desconto(1000)
    print(f"Desconto VIP: R$ {desconto_vip:.2f}")  # 200.00
    
    # Usar com desconto Premium
    calc_premium = CalculadoraDesconto(DescontoPremium())
    desconto_premium = calc_premium.calcular_desconto(1000)
    print(f"Desconto Premium: R$ {desconto_premium:.2f}")  # 150.00
    
    # Usar com desconto Regular
    calc_regular = CalculadoraDesconto(DescontoRegular())
    desconto_regular = calc_regular.calcular_desconto(1000)
    print(f"Desconto Regular: R$ {desconto_regular:.2f}")  # 50.00
    
    # ========================================================================
    # EXTENSIBILIDADE: Adicionar novo tipo SEM MODIFICAR código existente!
    # ========================================================================
    
    class DescontoEstudante(DescontoStrategy):
        """Novo tipo de desconto - apenas criamos uma nova classe!"""
        def calcular_desconto(self, valor):
            return valor * 0.10  # 10% para estudantes
    
    # Usar o novo desconto sem modificar CalculadoraDesconto!
    calc_estudante = CalculadoraDesconto(DescontoEstudante())
    desconto_estudante = calc_estudante.calcular_desconto(1000)
    print(f"Desconto Estudante: R$ {desconto_estudante:.2f}")  # 100.00

