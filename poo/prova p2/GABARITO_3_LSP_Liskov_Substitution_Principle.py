"""
================================================================================
GABARITO - SIMULADO P2 - PROGRAMAÇÃO ORIENTADA A OBJETOS
Professor: Tiago Castro
Turma: 4º Período B - Engenharia de Software
================================================================================

PRINCÍPIO: LISKOV SUBSTITUTION PRINCIPLE (LSP)
VALOR: 1,0 ponto

SOLUÇÃO CORRETA
================================================================================
"""

from abc import ABC, abstractmethod

# ============================================================================
# SOLUÇÃO APLICANDO O LSP
# ============================================================================
# 
# Agora Retangulo e Quadrado herdam de FormaGeometrica, não um do outro.
# Cada um mantém seu próprio comportamento, mas ambos podem ser usados
# onde FormaGeometrica é esperado.
#
# ============================================================================

class FormaGeometrica(ABC):
    """
    Classe abstrata que define o contrato comum para todas as formas geométricas.
    Qualquer função que receba FormaGeometrica pode trabalhar com qualquer
    implementação concreta (Retangulo, Quadrado, Circulo, etc).
    """
    @abstractmethod
    def calcular_area(self):
        """Calcula a área da forma geométrica"""
        pass


class Retangulo(FormaGeometrica):
    """
    Retangulo herda diretamente de FormaGeometrica.
    Mantém seu comportamento independente: largura e altura podem ser
    alteradas separadamente.
    """
    def __init__(self, largura, altura):
        self._largura = largura
        self._altura = altura
    
    def set_largura(self, largura):
        """Define a largura do retângulo"""
        self._largura = largura
    
    def set_altura(self, altura):
        """Define a altura do retângulo"""
        self._altura = altura
    
    def set_largura_e_altura(self, largura, altura):
        """Define largura e altura simultaneamente"""
        self._largura = largura
        self._altura = altura
    
    def get_largura(self):
        return self._largura
    
    def get_altura(self):
        return self._altura
    
    def calcular_area(self):
        """Calcula a área do retângulo"""
        return self._largura * self._altura


class Quadrado(FormaGeometrica):
    """
    Quadrado herda diretamente de FormaGeometrica, NÃO de Retangulo.
    Mantém seu próprio comportamento: lado único que define largura e altura.
    """
    def __init__(self, lado):
        self._lado = lado
    
    def set_lado(self, lado):
        """Define o lado do quadrado (afeta largura e altura igualmente)"""
        self._lado = lado
    
    def get_lado(self):
        return self._lado
    
    def calcular_area(self):
        """Calcula a área do quadrado"""
        return self._lado * self._lado


# ============================================================================
# EXEMPLO DE USO - FUNÇÃO QUE FUNCIONA COM QUALQUER FormaGeometrica
# ============================================================================

def dobrar_tamanho(forma: FormaGeometrica):
    """
    Esta função funciona com QUALQUER FormaGeometrica.
    Não precisa saber se é Retangulo ou Quadrado!
    """
    area_original = forma.calcular_area()
    
    # Para Retangulo, dobra largura e altura separadamente
    if isinstance(forma, Retangulo):
        forma.set_largura(forma.get_largura() * 2)
        forma.set_altura(forma.get_altura() * 2)
    # Para Quadrado, dobra o lado
    elif isinstance(forma, Quadrado):
        forma.set_lado(forma.get_lado() * 2)
    
    area_nova = forma.calcular_area()
    return area_nova


def calcular_area_total(formas: list[FormaGeometrica]):
    """
    Outro exemplo: função que calcula área total de várias formas.
    Funciona com qualquer combinação de FormaGeometrica!
    """
    total = 0
    for forma in formas:
        total += forma.calcular_area()
    return total


# ============================================================================
# TESTES
# ============================================================================

if __name__ == "__main__":
    # Teste com Retangulo
    r = Retangulo(5, 4)
    print(f"Retangulo original: {r.get_largura()}x{r.get_altura()} = área {r.calcular_area()}")
    area_dobrada = dobrar_tamanho(r)
    print(f"Retangulo dobrado: {r.get_largura()}x{r.get_altura()} = área {area_dobrada}")
    print(f"Esperado: 80 (10 * 8)\n")
    
    # Teste com Quadrado
    q = Quadrado(5)
    print(f"Quadrado original: lado {q.get_lado()} = área {q.calcular_area()}")
    area_dobrada = dobrar_tamanho(q)
    print(f"Quadrado dobrado: lado {q.get_lado()} = área {area_dobrada}")
    print(f"Esperado: 100 (10 * 10)\n")
    
    # Teste com lista mista (polimorfismo)
    formas = [
        Retangulo(3, 4),
        Quadrado(5),
        Retangulo(2, 6)
    ]
    area_total = calcular_area_total(formas)
    print(f"Área total de {len(formas)} formas: {area_total}")
    print(f"Esperado: 12 + 25 + 12 = 49")

