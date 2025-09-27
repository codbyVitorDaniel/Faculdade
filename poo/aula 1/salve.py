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
        """
        Construtor da classe Livro.
        TODO 2: Implemente o construtor inicializando todos os atributos 
                descritos no TODO 1. (Use EXATAMENTE ESSA NOMENCLATURA PARA OS ATRIBUTOS)
        """
        pass
    
    # TODO 3: Implemente os getters e setters para os atributos privados
    # - getter e setter para _isbn (PARA O SETTER USE O METODO ESTÁTICO validar_isbn)
    # - getter e setter para _disponivel (para o setter, o valor deve ser um booleano)
    # - Somente getter para _total_emprestimos (ESSE AQUI É APENAS LEITURA)
    
    def emprestar(self):
        """
        Método para emprestar o livro.
        TODO 4: Implemente a lógica:
        - Se o livro estiver disponível, marque como indisponível
        - Incremente o contador de empréstimos
        - RETORNE True se emprestado com sucesso, False caso contrário
        """
        pass
    
    def devolver(self):
        """
        Método para devolver o livro.
        TODO 5: Implemente a lógica:
        - Marque o livro como disponível
        - RETORNE True se devolvido com sucesso, False caso contrário
        """
        pass
    
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
        pass
    

    # TODO 7: Implemente um método de classe para criar livro de exemplo
    # O método deve retornar uma instância de Livro com dados de exemplo
    # O exemplo deve retornar: "titulo do livro",  "autor do livro", "isbn do livro"
    @classmethod
    def criar_livro_exemplo(cls):
        pass


# ===========================================
# PARTE 2: HERANÇA - LIVRO DIGITAL
# ===========================================

class LivroDigital(Livro):
    """
    Classe que herda de Livro para representar livros digitais.
    """
    
    def __init__(self, titulo, autor, isbn, tamanho_mb, formato):
        """
        Construtor da classe LivroDigital.
        TODO 8: Implemente o construtor:
        - Chame o construtor da classe pai (super().__init__(......))
        - Adicione os novos atributos COM EXATAMENTE ESSA NOMENCLATURA: 
                - tamanho_mb 
                - formato
        """
        pass
    
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
        """
        Retorna informações técnicas do livro digital.
        RETORNE: "Formato: [formato] - Tamanho: [tamanho_mb] MB"
        """
        pass


# ===========================================
# PARTE 3: HERANÇA - LIVRO FÍSICO
# ===========================================

class LivroFisico(Livro):
    """
    Classe que herda de Livro para representar livros físicos.
    """
    
    def __init__(self, titulo, autor, isbn, numero_paginas, localizacao):
        """
        Construtor da classe LivroFisico.
        TODO 11: Implemente o construtor:
        - Chame o construtor da classe pai (super().__init__(......))
        - Adicione os novos atributos COM EXATAMENTE ESSA NOMENCLATURA: 
                - numero_paginas 
                - localizacao
        """
        pass
    
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
        """
        Retorna informações físicas do livro.
        RETORNE : "Páginas: [numero_paginas] - Localização: [localizacao]"
        """
        pass


# ===========================================
# PARTE 4: POLIMORFISMO - BIBLIOTECA
# ===========================================

class Biblioteca:
    """
    Classe para gerenciar uma biblioteca com diferentes tipos de livros.
    AQUI NÃO PRECISA CHAMAR O CONSTRUTOR DA CLASSE PAI.
    """
    
    def __init__(self, nome):
        """
        Construtor da classe Biblioteca.
        TODO 14: Implemente o seguinte no construtor:
        - Inicialize o atributo: nome 
        - Inicialize uma LISTA vazia para armazenar os livros.
        """
        pass
    
    def adicionar_livro(self, livro):
        """
        Adiciona um livro à biblioteca.
        TODO 15: Implemente a lógica para adicionar um livro à lista
        """
        pass
    
    def listar_livros(self):
        """
        Lista todos os livros da biblioteca.
        TODO 16: Implemente a lógica para imprimir todos os livros
        Use polimorfismo - cada tipo de livro terá sua própria representação
        Printe o nome da biblioteca antes de imprimir os livros.
        Crie uma estrutura FOR para percorrer a lista de livros e printar todos no terminal.
        """
        pass
    
    def buscar_livro_por_titulo(self, titulo):
        """
        Busca um livro pelo título.
        TODO 17: Implemente a busca e retorne o primeiro livro encontrado
        Crie uma estrutura FOR para percorrer a lista de livros e buscar o livro pelo titulo.
        DICA: use o .lower() para comparar o titulo do livro com o titulo buscado.
        Se encontrado, retorne o livro.
        Se não encontrado, retorne None ou "Livro não encontrado".
        """
        pass
    
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
