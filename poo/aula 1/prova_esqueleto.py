# ===========================================
# Universidade de Vassouras - Campus Maricá
# SIMULADO - ORIENTAÇÃO A OBJETOS EM PYTHON 2025.1
# Prof. Tiago Ruiz de Castro 
# ===========================================
# LEIA TODAS AS INSTRUÇÕES COM ATENÇÃO ANTES DE COMEÇAR
# INSTRUÇÕES:
# 1. Complete o código abaixo implementando as funcionalidades solicitadas
# 2. Cada seção tem comentários indicando exatamente o que implementar
# 3. NÃO altere a estrutura básica, apenas complete as partes marcadas
# 4. Teste seu código antes de entregar
#
# CONCEITOS A SEREM APLICADOS:
# - Atributos (públicos e privados)
# - Métodos (instância, estáticos e de classe)
# - Herança
# - Polimorfismo
# - Encapsulamento (getters e setters)
# - Métodos Estáticos (@staticmethod)
# - Métodos de Classes (@classmethod)
#
# ===========================================

# ===========================================
# PARTE 1: CLASSE BASE LIVRO
# ===========================================

class Livro:
    """
    Classe base para representar um livro na biblioteca.
    Chamamos isso aqui também de classe mãe ou classe pai, ou de superclasse.
    """
    
    # TODO 1: Crie os atributos da classe (públicos e privados)
    # - titulo (público)
    # - autor (público) 
    # - _isbn (privado)
    # - _disponivel (privado)
    # - _total_emprestimos (privado)
    
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self._isbn = isbn
        self._disponivel = True
        self._total_emprestimos = 0
        """
        Construtor da classe Livro.
        TODO 2: Implemente o construtor inicializando todos os atributos 
                descritos no TODO 1. (Use EXATAMENTE ESSA NOMENCLATURA PARA OS ATRIBUTOS)
        """
    @property
    def isbn(self):
        return self._isbn
    @isbn.setter
    def isbn (self, valor):
        if self.validar_isbn:
            self._isbn = valor
        else:
            print("Invalido")
    @property
    def disponivel(self):
        return self._disponivel
    @disponivel.setter
    def disponivel(self,valor):
        if self.disponivel.isinstance(valor, bool):
            self._disponivel = valor
        else:
            print("Valor incorreto")
    
    @property
    def total_emprestimos(self):
        return self._total_emprestimos
    
    # TODO 3: Implemente os getters e setters para os atributos privados
    # - getter e setter para _isbn (PARA O SETTER USE O METODO ESTÁTICO validar_isbn)
    # - getter e setter para _disponivel (para o setter, o valor deve ser um booleano)
    # - Somente getter para _total_emprestimos (ESSE AQUI É APENAS LEITURA)
    
    def emprestar(self):
        if self._disponivel:
            self.disponivel = False
            self._total_emprestimos += 1
            return True
        else:
            return False    
        """
        Método para emprestar o livro.
        TODO 4: Implemente a lógica:
        - Se o livro estiver disponível, marque como indisponível
        - Incremente o contador de empréstimos
        - RETORNE True se emprestado com sucesso, False caso contrário
        """
    
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            return True
        else:
            print("Livro nao devolvido")
            return False
        """
        Método para devolver o livro.
        TODO 5: Implemente a lógica:
        - Marque o livro como disponível
        - RETORNE True se devolvido com sucesso, False caso contrário
        """
    
    def __str__(self):
        """
        Método especial para representação em string. (JÁ ESTÁ IMPLEMENTADO. NÃO ALTERE!)
        """
        status = "Sim" if self._disponivel else "Não"
        return f"Livro: {self.titulo} - Autor: {self.autor} - Disponível: {status}"

    
    # TODO 6: Implemente um método estático para validar ISBN
    # O método deve verificar se o ISBN tem exatamente 13 dígitos
    # Tem varias formas de fazer isso. 
    # Dica: se quiser, use a função .isdigit() e len() 
    @staticmethod
    def validar_isbn(isbn):
        if isbn.isdigit():
            digit = isbn.len()
            return digit
        else:
            print("Nao e numero")
    

    # TODO 7: Implemente um método de classe para criar livro de exemplo
    # O método deve retornar uma instância de Livro com dados de exemplo
    # O exemplo deve retornar: "titulo do livro",  "autor do livro", "isbn do livro"
    @classmethod
    def criar_livro_exemplo(cls):
        return cls("vitor", "Daniel", "123456")


# ===========================================
# PARTE 2: HERANÇA - LIVRO DIGITAL
# ===========================================

class LivroDigital(Livro):
    """
    Classe que herda de Livro para representar livros digitais.
    """
    def __init__(self, titulo, autor, isbn, tamanho_mb, formato):
        super().__init__(titulo, autor, isbn)
        self.tamanho_mb = tamanho_mb
        self.formato = formato
        """
        Construtor da classe LivroDigital.
        TODO 8: Implemente o construtor:
        - Chame o construtor da classe pai (super().__init__(......))
        - Adicione os novos atributos COM EXATAMENTE ESSA NOMENCLATURA: 
                - tamanho_mb 
                - formato
        """
    @property
    def tama_mb(self):
        return self.tamanho_mb
    @tama_mb.setter
    def tama_mb(self, valor):
        if valor > 0:
            self.tamanho_mb = valor
        else:
            print("Valor nao e maior que 0")
    
    @property
    def formato(self):
        return self.formato
    @formato.setter
    def formato(self,valor):
        if isinstance(valor, str):
            self.formato = valor
        else:
            print("O valor nao e uma string")
    # TODO 9: Implemente getters e setters para os novos atributos
    # - getter e setter para tamanho_mb ( para o setter, o valor deve ser positivo ou seja, maior que 0 )
    # - getter e setter para formato ( para o setter, o valor deve ser uma string )
    
    def __str__(self):
        """
        Método especial para representação em string. >> (JÁ ESTA IMPLEMENTADO. NÃO ALTERE.) <<
        """
        status = "Sim" if self.disponivel else "Não"
        return f"Livro Digital: {self.titulo} - Autor: {self.autor} - Formato: {self.formato} - Disponível: {status}"

    
    # TODO 10: Implemente um método específico para livros digitais
    def obter_informacoes_tecnica(self):
        return f"Formato:{self.formato} - tamanho: {self.tamanho_mb} MB"
        """
        Retorna informações técnicas do livro digital.
        RETORNE: "Formato: [formato] - Tamanho: [tamanho_mb] MB"
        """


# ===========================================
# PARTE 3: HERANÇA - LIVRO FÍSICO
# ===========================================

class LivroFisico(Livro):
    """
    Classe que herda de Livro para representar livros físicos.
    """
    def __init__(self, titulo, autor, isbn, numero_paginas, localizacao):
        super().__init__(titulo, autor, isbn)
        self.numero_paginas = numero_paginas
        self.localizacao = localizacao
        """
        Construtor da classe LivroFisico.
        TODO 11: Implemente o construtor:
        - Chame o construtor da classe pai (super().__init__(......))
        - Adicione os novos atributos COM EXATAMENTE ESSA NOMENCLATURA: 
                - numero_paginas 
                - localizacao
        """
    @property
    def numero_pro(self):
        return self.numero_paginas
    
    @numero_pro.setter
    def numero_pro(self,valor):
        self.numero_paginas = valor
    
    @property
    def localizacao_pro(self):
        return self.localizacao
    @localizacao_pro.setter
    def localizacao_pro(self,valor):
        self.localizacao = valor

    # TODO 12: Implemente getters e setters para os novos atributos
    # - getter e setter para numero_paginas
    # - getter e setter para localizacao
    

    #Aqui eu ja implementei o metodo especial para representação em string.
    def __str__(self):
        """
        Método especial para representação em string. (JÁ ESTÁ IMPLEMENTADO. NÃO ALTERE!)
        """
        status = "Sim" if self.disponivel else "Não"
        return f"Livro Físico: {self.titulo} - Autor: {self.autor} - Páginas: {self.numero_paginas} - Disponível: {status}"


    
    # TODO 13: Implemente um método específico para livros físicos
    def obter_informacoes_fisicas(self):
        return f"Paginas:{self.numero_paginas} - Localizaçao: {self.localizacao}"
        """
        Retorna informações físicas do livro.
        RETORNE : "Páginas: [numero_paginas] - Localização: [localizacao]"
        """
        


# ===========================================
# PARTE 4: POLIMORFISMO - BIBLIOTECA
# ===========================================

class Biblioteca:
    """
    Classe para gerenciar uma biblioteca com diferentes tipos de livros.
    AQUI NÃO PRECISA CHAMAR O CONSTRUTOR DA CLASSE PAI.
    """
    
    def __init__(self, nome):
        self.nome = nome
        self.lista = []
        """
        Construtor da classe Biblioteca.
        TODO 14: Implemente o seguinte no construtor:
        - Inicialize o atributo: nome 
        - Inicialize uma LISTA vazia para armazenar os livros.
        """
    
    def adicionar_livro(self, livro):
        self.lista.append(livro)
        """
        Adiciona um livro à biblioteca.
        TODO 15: Implemente a lógica para adicionar um livro à lista
        """
    
    def listar_livros(self):
        for livro in self.lista:
            for i in livro:
                print(f"Livros {livro} na {i}")
        """
        Lista todos os livros da biblioteca.
        TODO 16: Implemente a lógica para imprimir todos os livros
        Use polimorfismo - cada tipo de livro terá sua própria representação
        Printe o nome da biblioteca antes de imprimir os livros.
        Crie uma estrutura FOR para percorrer a lista de livros e printar todos no terminal.
        """
    
    def buscar_livro_por_titulo(self, titulo):
        buscar = input("Digite o nome do Livro\nR:")
        titulo
        for lista 
        """
        Busca um livro pelo título.
        TODO 17: Implemente a busca e retorne o primeiro livro encontrado
        Crie uma estrutura FOR para percorrer a lista de livros e buscar o livro pelo titulo.
        DICA: use o .lower() para comparar o titulo do livro com o titulo buscado.
        Se encontrado, retorne o livro.
        Se não encontrado, retorne None ou "Livro não encontrado".
        """
        
    
    def emprestar_livro(self, titulo):
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
        """
        Devolve um livro pelo título.
        TODO 19: Implemente a lógica:
        - Busque o livro pelo título (use o metodo buscar_livro_por_titulo() ja criado)
        - Se encontrado, tente devolvê-lo (mensagem de retorno: "Livro devolvido com sucesso!")
        - Se ja estiver devolvido, retorne "Livro ja estava disponível"
        - Se não encontrado pelo titulo, retorne "Livro não disponível na biblioteca"
        - Fique a vontade para criar uma mensagem legal.
        """
        pass
    
    # TODO 20: Implemente um método estático para validar nome da biblioteca
    # O método deve verificar se o nome da biblioteca é válido (não vazio e sem números)
    # Dica1: use a função .isalpha() para verificar se o nome da biblioteca é apenas letras.
    # Dica2: use a função .strip() para remover espaços em branco.
    # Dica3: use isinstance(nome, str) para verificar se o nome é uma string.
    # Implemente a logica que quiser, mas deve retornar True se o nome da biblioteca for válido, False caso contrário.
    @staticmethod
    def validar_nome_biblioteca(nome):
        """
        Valida se o nome da biblioteca é válido (não vazio e sem números).
        """
        pass
    


    #Aqui eu ja implementei o metodo de classe para criar biblioteca de exemplo.
    @classmethod
    def criar_biblioteca_exemplo(cls):
        """
        Aqui eu implementei uma biblioteca de exemplo com alguns livros.(JA ESTA IMPLEMENTADO. NÃO ALTERE.)
        """
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

# ===========================================
# PARTE 5: TESTE DO SISTEMA
# ===========================================

def testar_sistema():
    """
    Função para testar o sistema implementado.
    TODO 21: Implemente os testes:
    1. Crie uma biblioteca

    2. Adicione livros de diferentes tipos

    3. Teste empréstimos e devoluções

    4. Liste os livros

    5. Teste buscas
    
    """
    pass


# ===========================================
# EXECUÇÃO PRINCIPAL
# ===========================================

if __name__ == "__main__":
    print("=== SIMULADO - ORIENTAÇÃO A OBJETOS ===")
    print("Complete todas as implementações marcadas com TODO")
    print("Execute testar_sistema() para testar sua implementação")
    print("=" * 40)
    
    # Descomente a linha abaixo para testar
    # testar_sistema()
