"""
================================================================================
GABARITO - SIMULADO P2 - PROGRAMAÇÃO ORIENTADA A OBJETOS
Professor: Tiago Castro
Turma: 4º Período B - Engenharia de Software
================================================================================

PRINCÍPIO: INTERFACE SEGREGATION PRINCIPLE (ISP)
VALOR: 2,0 pontos

SOLUÇÃO CORRETA
================================================================================
"""

from abc import ABC, abstractmethod

# ============================================================================
# SOLUÇÃO APLICANDO O ISP
# ============================================================================
# 
# Interfaces segregadas: cada interface tem uma responsabilidade específica.
# Classes implementam apenas as interfaces que realmente precisam.
#
# ============================================================================

class Trabalhador(ABC):
    """
    Interface específica para quem trabalha.
    Apenas define o método trabalhar().
    """
    @abstractmethod
    def trabalhar(self):
        """Método para trabalhar"""
        pass


class SerVivo(ABC):
    """
    Interface específica para seres vivos.
    Define métodos relacionados a necessidades biológicas.
    """
    @abstractmethod
    def comer(self):
        """Método para comer"""
        pass
    
    @abstractmethod
    def dormir(self):
        """Método para dormir"""
        pass


class Humano(Trabalhador, SerVivo):
    """
    Humano implementa AMBAS as interfaces porque:
    - Humanos trabalham (Trabalhador)
    - Humanos comem e dormem (SerVivo)
    """
    def trabalhar(self):
        return "Humano trabalhando..."
    
    def comer(self):
        return "Humano comendo..."
    
    def dormir(self):
        return "Humano dormindo..."


class Robo(Trabalhador):
    """
    Robo implementa APENAS a interface Trabalhador.
    Não precisa implementar SerVivo porque robos não comem nem dormem.
    Agora não é forçado a implementar métodos que não fazem sentido!
    """
    def trabalhar(self):
        return "Robo trabalhando..."


# ============================================================================
# EXEMPLO DE USO
# ============================================================================

def fazer_trabalhar(trabalhador: Trabalhador):
    """
    Função que funciona com qualquer Trabalhador.
    Não precisa saber se é Humano ou Robo.
    """
    return trabalhador.trabalhar()


def fazer_comer_e_dormir(ser_vivo: SerVivo):
    """
    Função que funciona apenas com SerVivo.
    Robo não pode ser passado aqui (e não deveria mesmo!).
    """
    return f"{ser_vivo.comer()} Depois {ser_vivo.dormir()}"


# ============================================================================
# TESTES
# ============================================================================

if __name__ == "__main__":
    # Criar instâncias
    humano = Humano()
    robo = Robo()
    
    # Humanos podem trabalhar, comer e dormir
    print("=== HUMANO ===")
    print(humano.trabalhar())  # OK
    print(humano.comer())      # OK
    print(humano.dormir())     # OK
    print()
    
    # Robos podem apenas trabalhar
    print("=== ROBO ===")
    print(robo.trabalhar())    # OK
    # robo.comer()             # ERRO! Método não existe (e não deveria existir)
    # robo.dormir()            # ERRO! Método não existe (e não deveria existir)
    print()
    
    # Polimorfismo com Trabalhador
    print("=== POLIMORFISMO ===")
    trabalhadores = [humano, robo]
    for trabalhador in trabalhadores:
        print(fazer_trabalhar(trabalhador))
    print()
    
    # Polimorfismo com SerVivo (apenas Humano)
    print("=== SERES VIVOS ===")
    seres_vivos = [humano]  # Robo não pode estar aqui!
    for ser_vivo in seres_vivos:
        print(fazer_comer_e_dormir(ser_vivo))
    
    # ========================================================================
    # EXTENSIBILIDADE: Adicionar novos tipos
    # ========================================================================
    
    class Animal(SerVivo):
        """Animal é SerVivo mas não Trabalhador"""
        def comer(self):
            return "Animal comendo..."
        
        def dormir(self):
            return "Animal dormindo..."
    
    class RoboAvancado(Trabalhador, SerVivo):
        """
        Robo avançado que pode trabalhar E "comer" (recarregar) e "dormir" (modo standby).
        Implementa ambas as interfaces porque faz sentido para ele.
        """
        def trabalhar(self):
            return "Robo avançado trabalhando..."
        
        def comer(self):
            return "Robo avançado recarregando bateria..."
        
        def dormir(self):
            return "Robo avançado em modo standby..."
    
    print("\n=== EXTENSIBILIDADE ===")
    animal = Animal()
    robo_avancado = RoboAvancado()
    
    print(animal.comer())
    print(robo_avancado.trabalhar())
    print(robo_avancado.comer())

