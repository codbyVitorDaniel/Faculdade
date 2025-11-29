# """
# ================================================================================
# PROVA P2 - PROGRAMAÇÃO ORIENTADA A OBJETOS
# Professor: Tiago Castro
# Turma: 4º Período - Engenharia de Software
# Universidade de Vassouras
# ================================================================================

# QUESTÃO 1: PRINCÍPIOS SOLID - SRP, OCP e LSP
# VALOR: 5,0 pontos (se respeitado todos os princípios)

# TEMA: SISTEMA DE BIBLIOTECA - GERENCIAMENTO DE EMPRÉSTIMOS

# Refatore o código abaixo aplicando os três princípios SOLID simultaneamente.

# ================================================================================
# """

# # ============================================================================
# # CÓDIGO QUE VIOLA OS PRINCÍPIOS SRP, OCP e LSP
# # ============================================================================

# class Livro:
#     def __init__(self, isbn, titulo, autor):
#         self.isbn = isbn
#         self.titulo = titulo
#         self.autor = autor
#         self.disponivel = True
#         self.emprestado_para = None
#         self.dias_emprestimo = 7
    
#     def emprestar(self, usuario):
#         if not self.disponivel:
#             return False
#         self.disponivel = False
#         self.emprestado_para = usuario
#         return True
    
#     def renovar(self):
#         if self.disponivel:
#             return False
#         self.dias_emprestimo += 7
#         return True
    
#     def devolver(self):
#         if self.disponivel:
#             return False
#         self.disponivel = True
#         self.emprestado_para = None
#         return True


# class LivroDigital(Livro):
#     """PROBLEMA LSP: Herda de Livro mas sempre retorna False em renovar()"""
#     def __init__(self, isbn, titulo, autor, url_download):
#         super().__init__(isbn, titulo, autor)
#         self.url_download = url_download
    
#     def renovar(self):
#         return False  # Viola LSP: quebra o contrato de Livro


# class EmprestimoService:
#     """
#     PROBLEMA SRP: Múltiplas responsabilidades (empréstimo, multa, banco, email)
#     PROBLEMA OCP: calcular_multa precisa ser modificado para novos tipos
#     """
#     def __init__(self):
#         self.emprestimos = []
    
#     def realizar_emprestimo(self, livro, usuario, tipo_usuario):
#         if not livro.disponivel:
#             return False
        
#         livro.emprestar(usuario)
#         self.emprestimos.append({'livro': livro, 'usuario': usuario, 'tipo_usuario': tipo_usuario})
#         self.salvar_no_banco(livro, usuario)  # SRP: responsabilidade de persistência
#         self.enviar_email_confirmacao(usuario, livro)  # SRP: responsabilidade de notificação
#         return True
    
#     def calcular_multa(self, dias_atraso, tipo_usuario):
#         """PROBLEMA OCP: Precisa modificar para adicionar novos tipos"""
#         if tipo_usuario == "ALUNO_GRADUACAO":
#             return dias_atraso * 2.0
#         elif tipo_usuario == "ALUNO_POS":
#             return dias_atraso * 1.5
#         elif tipo_usuario == "FUNCIONARIO":
#             return dias_atraso * 3.0
#         else:
#             return 0
    
#     def salvar_no_banco(self, livro, usuario):
#         print(f"Salvando empréstimo do livro '{livro.titulo}' para {usuario} no banco...")
    
#     def enviar_email_confirmacao(self, usuario, livro):
#         print(f"Enviando email para {usuario} confirmando empréstimo de '{livro.titulo}'")
    
#     def processar_renovacao(self, livro):
#         """PROBLEMA LSP: Pode receber LivroDigital que quebra o comportamento"""
#         if livro.disponivel:
#             return False
#         sucesso = livro.renovar()
#         if sucesso:
#             print(f"Livro '{livro.titulo}' renovado com sucesso!")
#             self.salvar_no_banco(livro, livro.emprestado_para)
#         return sucesso


# ============================================================================
# ORIENTAÇÕES PARA CORREÇÃO
# ============================================================================
#
# 1. SRP:
#    - Separe EmprestimoService: crie LivroRepository (persistência) e EmailService (notificações)
#    - Mantenha EmprestimoService apenas para lógica de empréstimo
#
# 2. OCP:
#    - Crie interface EstrategiaMulta (ABC) com calcular_multa()
#    - Crie classes: MultaAlunoGraduacao, MultaAlunoPos, MultaFuncionario
#    - Use injeção de dependência em EmprestimoService
#
# 3. LSP:
#    - Crie MaterialBiblioteca (ABC) com emprestar() e devolver()
#    - Crie interface Renovavel (ABC) com renovar()
#    - Livro implementa MaterialBiblioteca + Renovavel
#    - LivroDigital implementa apenas MaterialBiblioteca
#
# ============================================================================
# ÁREA PARA SUA IMPLEMENTAÇÃO
# ============================================================================

# TODO: Implemente aqui sua solução aplicando SRP, OCP e LSP



# Implemente aqui o exemplo de uso:
from abc import ABC, abstractmethod

# =============================================================
# LSP — Interfaces corretas para cada tipo de material
# =============================================================

class MaterialBiblioteca(ABC):
    @abstractmethod
    def emprestar(self, usuario):
        pass

    @abstractmethod
    def devolver(self):
        pass


class Renovavel(ABC):
    @abstractmethod
    def renovar(self):
        pass




class Livro(MaterialBiblioteca, Renovavel):
    """Agora Livro pode ser renovado sem quebrar LSP"""
    def __init__(self, isbn, titulo, autor):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
        self.emprestado_para = None
        self.dias_emprestimo = 7

    def emprestar(self, usuario):
        if not self.disponivel:
            return False
        self.disponivel = False
        self.emprestado_para = usuario
        return True

    def renovar(self):
        if self.disponivel:
            return False
        self.dias_emprestimo += 7
        return True

    def devolver(self):
        if self.disponivel:
            return False
        self.disponivel = True
        self.emprestado_para = None
        return True


class LivroDigital(MaterialBiblioteca):
    """Livro digital agora NÃO é renovável (não implementa Renovavel)"""
    def __init__(self, isbn, titulo, autor, url_download):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.url_download = url_download
        self.disponivel = True
        self.emprestado_para = None

    def emprestar(self, usuario):
        if not self.disponivel:
            return False
        self.disponivel = False
        self.emprestado_para = usuario
        return True

    def devolver(self):
        if self.disponivel:
            return False
        self.disponivel = True
        self.emprestado_para = None
        return True



class EstrategiaMulta(ABC):
    @abstractmethod
    def calcular_multa(self, dias_atraso):
        pass


class MultaAlunoGraduacao(EstrategiaMulta):
    def calcular_multa(self, dias_atraso):
        return dias_atraso * 2.0


class MultaAlunoPos(EstrategiaMulta):
    def calcular_multa(self, dias_atraso):
        return dias_atraso * 1.5


class MultaFuncionario(EstrategiaMulta):
    def calcular_multa(self, dias_atraso):
        return dias_atraso * 3.0




class LivroRepository:
    def salvar_emprestimo(self, livro, usuario):
        print(f"[DB] Salvando empréstimo de '{livro.titulo}' para {usuario}.")


class EmailService:
    def enviar_email_confirmacao(self, usuario, livro):
        print(f"[EMAIL] Enviando email para {usuario}: Empréstimo de '{livro.titulo}' confirmado!")




class EmprestimoService:
    def __init__(self, repository: LivroRepository, email: EmailService, estrategia_multa: EstrategiaMulta):
        self.repository = repository
        self.email = email
        self.estrategia_multa = estrategia_multa

    def realizar_emprestimo(self, material: MaterialBiblioteca, usuario):
        if not material.emprestar(usuario):
            return False

        self.repository.salvar_emprestimo(material, usuario)
        self.email.enviar_email_confirmacao(usuario, material)
        return True

    def processar_renovacao(self, material: MaterialBiblioteca):
        """Só renova se o material for Renovavel (LSP)"""
        if isinstance(material, Renovavel):
            sucesso = material.renovar()
            if sucesso:
                self.repository.salvar_emprestimo(material, material.emprestado_para)
            return sucesso
        return False 

    def calcular_multa(self, dias_atraso):
        return self.estrategia_multa.calcular_multa(dias_atraso)




if __name__ == "__main__":
    livro = Livro("123", "O Hobbit", "Tolkien")
    ebook = LivroDigital("999", "Python Avançado", "Guido", "http://download/pdf")

    repo = LivroRepository()
    email = EmailService()

    estrategia = MultaAlunoGraduacao()

    service = EmprestimoService(repo, email, estrategia)

    print("\nEmpréstimo de livro físico")
    service.realizar_emprestimo(livro, "João")

    print("\nRenovação do livro físico")
    print(service.processar_renovacao(livro))

    print("\nEmpréstimo de livro digital")
    service.realizar_emprestimo(ebook, "Maria")

    print("\nTentando renovar livro digital")
    print(service.processar_renovacao(ebook))

    print("\nMulta para aluno de graduação")
    print("Multa:R$",service.calcular_multa(3))


















