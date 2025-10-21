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

<<<<<<< HEAD
        """
        Lista todos os livros da biblioteca.
        TODO 16: Implemente a lógica para imprimir todos os livros
        Use polimorfismo - cada tipo de livro terá sua própria representação
        Printe o nome da biblioteca antes de imprimir os livros.
        Crie uma estrutura FOR para percorrer a lista de livros e printar todos no terminal.
        """
    
    def buscar_livro_por_titulo(self, titulo):
        self.titulo = titulo.lower()
        for li in self.lista:
            for titu in titulo:
                if li == titu:
                    busca = li
                    print(f"Livro encontrado {busca}")
                    return True
                else:
                    print("Livro nao encontrado")
                    return False
        """
        Busca um livro pelo título.
        TODO 17: Implemente a busca e retorne o primeiro livro encontrado
        Crie uma estrutura FOR para percorrer a lista de livros e buscar o livro pelo titulo.
        DICA: use o .lower() para comparar o titulo do livro com o titulo buscado.
        Se encontrado, retorne o livro.
        Se não encontrado, retorne None ou "Livro não encontrado".
        """
        
    
    def emprestar_livro(self, titulo):
        self.titulo = titulo.lower()
        buscar = Biblioteca.buscar_livro_por_titulo(self.titulo)
        if buscar == True:
            print ("Emprestimo")
        elif buscar == False:
            print("Livro nao disponivel na biblioteca")
        else:
            print("Livro nao esta disponivel na biblioteca")
        """
        Empresta um livro pelo título.
        TODO 18: Implemente a lógica:
        - Busque o livro pelo título (use o metodo buscar_livro_por_titulo() ja criado)
        - Se encontrado, tente emprestá-lo
        - Se nao estiver disponível, retorne "Livro não esta disponível para empréstimo"
        - Se não encontrado, retorne "Livro não disponível na biblioteca"
        - Fique a vontade para criar uma mensagem legal.
        """
        pass
    
    def devolver_livro(self, titulo):
        self.titulo = titulo
        buscar = Biblioteca.buscar_livro_por_titulo(self.titulo)
        if buscar == True:
            print("Livro devolvido com sucesso!")

        elif buscar == False:
            print("Livro ja estava disponivel")
        else:
            print("Livro nao disponivel na biblioteca")
        """
        Devolve um livro pelo título.
        TODO 19: Implemente a lógica:
        - Busque o livro pelo título (use o metodo buscar_livro_por_titulo() ja criado)
        - Se encontrado, tente devolvê-lo (mensagem de retorno: "Livro devolvido com sucesso!")
        - Se ja estiver devolvido, retorne "Livro ja estava disponível"
        - Se não encontrado pelo titulo, retorne "Livro não disponível na biblioteca"
        - Fique a vontade para criar uma mensagem legal.
        """

    
    # TODO 20: Implemente um método estático para validar nome da biblioteca
    # O método deve verificar se o nome da biblioteca é válido (não vazio e sem números)
    # Dica1: use a função .isalpha() para verificar se o nome da biblioteca é apenas letras.
    # Dica2: use a função .strip() para remover espaços em branco.
    # Dica3: use isinstance(nome, str) para verificar se o nome é uma string.
    # Implemente a logica que quiser, mas deve retornar True se o nome da biblioteca for válido, False caso contrário.
    @staticmethod
    def validar_nome_biblioteca(self,nome):
        self.nome = nome.strip()
        if not self.nome.isalpha():
            print("Digite apenas letras")
            return False
        else:
            return True
        
        """
        Valida se o nome da biblioteca é válido (não vazio e sem números).
        """
    
=======
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
>>>>>>> 528b2f2d6f2888bd9f87e542da58aa61b8253a64

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
<<<<<<< HEAD

    biblioteca.listar_livros()
    print(biblioteca.emprestar_livro("Python Avançado"))
    print(biblioteca.emprestar_livro("Python Avançado"))
    print(biblioteca.devolver_livro("Python Avançado"))
    print(biblioteca.devolver_livro("Python Avançado"))
    print(biblioteca.buscar_livro_por_titulo("Algoritmos"))
    print(biblioteca.emprestar_livro("Livro Inexistente"))

    """
    Função para testar o sistema implementado.
    TODO 21: Implemente os testes:
    1. Crie uma biblioteca
=======
>>>>>>> 528b2f2d6f2888bd9f87e542da58aa61b8253a64

    # Listando livros
    biblioteca.listar_livros()

    # Emprestando livro
    print(biblioteca.emprestar_livro("Python Avançado"))

    # Devolvendo livro
    print(biblioteca.devolver_livro("Python Avançado"))

<<<<<<< HEAD
    5. Teste buscas 
    
    """
    pass
=======
    # Buscando livro
    livro_encontrado = biblioteca.buscar_livro_por_titulo("Orientação a Objetos")
    print(livro_encontrado)
>>>>>>> 528b2f2d6f2888bd9f87e542da58aa61b8253a64

    # Emprestando livro novamente
    print(biblioteca.emprestar_livro("Estruturas de Dados"))


if __name__ == "__main__":
    print("=== SIMULADO - ORIENTAÇÃO A OBJETOS ===")
    print("Complete todas as implementações marcadas com TODO")
    print("Execute testar_sistema() para testar sua implementação")
    print("=" * 40)
    
    # Descomente a linha abaixo para testar
    testar_sistema()
