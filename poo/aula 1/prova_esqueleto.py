class Livro:
    """
    Classe base para representar um livro na biblioteca.
    Chamamos isso aqui também de classe mãe ou classe pai, ou de superclasse.
    """
    
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self._isbn = isbn
        self._disponivel = True
        self._total_emprestimos = 0
    
    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, valor):
        if Livro.validar_isbn(valor):
            self._isbn = valor
        else:
            print("ISBN inválido. Deve ter 13 dígitos.")

    @property
    def disponivel(self):
        return self._disponivel

    @disponivel.setter
    def disponivel(self, valor):
        if isinstance(valor, bool):
            self._disponivel = valor
        else:
            print("Valor de disponibilidade inválido. Deve ser booleano.")
    
    @property
    def total_emprestimos(self):
        return self._total_emprestimos
    
    def emprestar(self):
        if self._disponivel:
            self.disponivel = False
            self._total_emprestimos += 1
            return True
        else:
            return False
    
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            return True
        else:
            print("Livro não devolvido")
            return False
    
    def __str__(self):
        status = "Sim" if self._disponivel else "Não"
        return f"Livro: {self.titulo} - Autor: {self.autor} - Disponível: {status}"

    @staticmethod
    def validar_isbn(isbn):
        return len(isbn) == 13 and isbn.isdigit()

    @classmethod
    def criar_livro_exemplo(cls):
        return cls("vitor", "Daniel", "123456")


class LivroDigital(Livro):
    def __init__(self, titulo, autor, isbn, tamanho_mb, formato):
        super().__init__(titulo, autor, isbn)
        self._tamanho_mb = tamanho_mb
        self._formato = formato

    @property
    def tamanho_mb(self):
        return self._tamanho_mb

    @tamanho_mb.setter
    def tamanho_mb(self, valor):
        if valor > 0:
            self._tamanho_mb = valor
        else:
            print("Tamanho inválido. Deve ser maior que 0.")
    
    @property
    def formato(self):
        return self._formato

    @formato.setter
    def formato(self, valor):
        if isinstance(valor, str):
            self._formato = valor
        else:
            print("Formato inválido. Deve ser uma string.")
    
    def __str__(self):
        status = "Sim" if self.disponivel else "Não"
        return f"Livro Digital: {self.titulo} - Autor: {self.autor} - Formato: {self._formato} - Disponível: {status}"
    
    def obter_informacoes_tecnica(self):
        return f"Formato:{self._formato} - Tamanho: {self._tamanho_mb} MB"


class LivroFisico(Livro):
    def __init__(self, titulo, autor, isbn, numero_paginas, localizacao):
        super().__init__(titulo, autor, isbn)
        self._numero_paginas = numero_paginas
        self._localizacao = localizacao

    @property
    def numero_paginas(self):
        return self._numero_paginas
    
    @numero_paginas.setter
    def numero_paginas(self, valor):
        if valor > 0:
            self._numero_paginas = valor
        else:
            print("Número de páginas inválido.")

    @property
    def localizacao(self):
        return self._localizacao
    
    @localizacao.setter
    def localizacao(self, valor):
        if isinstance(valor, str):
            self._localizacao = valor
        else:
            print("Localização inválida. Deve ser uma string.")
    
    def __str__(self):
        status = "Sim" if self.disponivel else "Não"
        return f"Livro Físico: {self.titulo} - Autor: {self.autor} - Páginas: {self._numero_paginas} - Disponível: {status}"

    def obter_informacoes_fisicas(self):
        return f"Páginas: {self._numero_paginas} - Localização: {self._localizacao}"


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.lista = []

    def adicionar_livro(self, livro):
        self.lista.append(livro)
    
    def listar_livros(self):
        print(f"Livros da {self.nome}:")
        for livro in self.lista:
            print(livro)

    def buscar_livro_por_titulo(self, titulo):
        for livro in self.lista:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return "Livro não encontrado"
    
    def emprestar_livro(self, titulo):
        livro = self.buscar_livro_por_titulo(titulo)
        if isinstance(livro, Livro):
            if livro.emprestar():
                return f"Livro '{titulo}' emprestado com sucesso!"
            else:
                return "Livro não disponível para empréstimo."
        return "Livro não disponível na biblioteca."

    def devolver_livro(self, titulo):
        livro = self.buscar_livro_por_titulo(titulo)
        if isinstance(livro, Livro):
            if livro.devolver():
                return f"Livro '{titulo}' devolvido com sucesso!"
            else:
                return "Livro já estava disponível."
        return "Livro não encontrado na biblioteca."

    @staticmethod
    def validar_nome_biblioteca(nome):
        return isinstance(nome, str) and nome.strip().isalpha()

    @classmethod
    def criar_biblioteca_exemplo(cls):
        biblioteca = cls("Biblioteca Central")
        
        # Adicionando livros de exemplo
        livro1 = LivroFisico("Orientação a Objetos", "Maria Santos", "1111111111111", 300, "Estante A-1")
        livro2 = LivroDigital("Python Avançado", "Carlos Lima", "2222222222222", 15.5, "PDF")
        livro3 = LivroFisico("Estruturas de Dados", "Ana Costa", "3333333333333", 450, "Estante B-2")
        livro4 = LivroDigital("Algoritmos", "Pedro Oliveira", "4444444444444", 22.3, "EPUB")
        
        biblioteca.adicionar_livro(livro1)
        biblioteca.adicionar_livro(livro2)
        biblioteca.adicionar_livro(livro3)
        biblioteca.adicionar_livro(livro4)
        
        return biblioteca


def testar_sistema():
    biblioteca = Biblioteca.criar_biblioteca_exemplo()

    # Listando livros
    biblioteca.listar_livros()

    # Emprestando livro
    print(biblioteca.emprestar_livro("Python Avançado"))

    # Devolvendo livro
    print(biblioteca.devolver_livro("Python Avançado"))

    # Buscando livro
    livro_encontrado = biblioteca.buscar_livro_por_titulo("Orientação a Objetos")
    print(livro_encontrado)

    # Emprestando livro novamente
    print(biblioteca.emprestar_livro("Estruturas de Dados"))


if __name__ == "__main__":
    print("=== SIMULADO - ORIENTAÇÃO A OBJETOS ===")
    print("Complete todas as implementações marcadas com TODO")
    print("Execute testar_sistema() para testar sua implementação")
    print("=" * 40)
    
    # Descomente a linha abaixo para testar
    testar_sistema()
