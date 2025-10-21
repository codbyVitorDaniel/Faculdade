# ===========================================
# Universidade de Vassouras - Campus Maricá
# PROVA P1 - ORIENTAÇÃO A OBJETOS EM PYTHON 2025.2
# Prof. Tiago Ruiz de Castro 
# ===========================================
#   LEIA TODAS AS INSTRUÇÕES COM ATENÇÃO ANTES DE COMEÇAR
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
# QUESTÃO 1: CLASSE BASE VEÍCULO (2.0 pontos)
# ===========================================

class Veiculo:
    """
    Classe base para representar um veículo.
    Chamamos isso aqui também de classe mãe ou classe pai, ou de superclasse.
    """
    
    # TODO 1: Crie os atributos da classe (públicos e privados)
    # - marca (público)
    # - modelo (público) 
    # - _ano (privado)
    # - _quilometragem (privado)
    # - _ligado (booleano)(privado)
    
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self._ano = ano
        self._quilometragem = 0
        self._ligado = False
        """
        Construtor da classe Veiculo.
        TODO 2: Implemente o construtor inicializando todos os atributos 
                descritos no TODO 1. (Use EXATAMENTE ESSA NOMENCLATURA PARA OS ATRIBUTOS)
        - _quilometragem deve começar com 0
        - _ligado deve começar com False
        APAGUE O PASS E ESCREVA SEU CODIGO ABAIXO:
        """
        @property
        def ano(self):
            return self._ano
        @ano.setter
        def ano(self,valor):
            if self._ano > 1900:
                self.ano = valor
            else:
                raise ValueError("Nao pode ser maior que 1900")
        
        @property
        def quilometragem(self):
            return self._quilometragem
        @quilometragem.setter
        def quilometragem(self,valor):
            if self._qui_quilometragem >= 0:
                self._quilometragem = valor
            else:
                raise ValueError("A quilometragem nao pode ser 0")
    # TODO 3: Implemente os getters e setters para os atributos privados
    # - getter e setter para _ano (para o setter, o ano deve ser maior que 1900 ,SE NAO RETORNE UM ERRO)
    # - getter e setter para _quilometragem (para o setter, deve ser >= 0, SE NAO RETORNE UM ERRO)
    # - Somente getter para _ligado (ESSE AQUI É APENAS LEITURA)
    
    def ligar(self):
        if not self._ligado:
            self._ligado = True
            return  True
        return False
        """
        Método para ligar o veículo.
        TODO 4: Implemente a lógica:
        - Se o veículo não estiver ligado, marque como ligado
        - RETORNE True se ligado com sucesso, False CASO CARRO JA ESTIVER LIGADO.
        APAGUE O PASS E ESCREVA SEU CODIGO ABAIXO:
        """
       
    def desligar(self):
        
        if self._ligado:
            self._ligado = False
            return  True
        return False
        """
        Método para desligar o veículo.
        TODO 5: Implemente a lógica:
        - Se o veículo estiver ligado, marque como desligado
        - RETORNE True se desligado com sucesso, False CASO CARRO JA ESTIVER DESLIGADO.
        APAGUE O PASS E ESCREVA SEU CODIGO ABAIXO:
        """
    
    def __str__(self):
        """
        ATENÇÃO:
        Método especial para representação em string. (JÁ ESTÁ IMPLEMENTADO. NÃO ALTERE!)
        """
        status = "Ligado" if self._ligado else "Desligado"
        return f"Veículo: {self.marca} {self.modelo} ({self._ano}) - {status} - {self._quilometragem} km"

    
    # TODO 6: Implemente um método estático para validar ano
    # O método deve verificar se o ano é válido (VERIFIQUE SE O ANO ESTA ENTRE 1900 e 2025)
    # APAGUE O PASS E ESCREVA SEU CODIGO ABAIXO:
    @staticmethod
    def validar_ano(ano):
        if isinstance(ano, int) and 1900 <= ano <= 2025:
            return True
        return False
        
    
    # TODO 7: Implemente um método de classe para criar veículo de exemplo
    # O método deve retornar uma instância de Veiculo com dados de exemplo
    # O exemplo deve retornar apenas: "Toyota", "Corolla", 2020
    # APAGUE O PASS E ESCREVA SEU CODIGO ABAIXO:
    @classmethod
    def criar_veiculo_exemplo(cls):
        cls("Toyota", "Corolla", 2020)



# ===========================================
# QUESTÃO 2: HERANÇA - CARRO (2.0 pontos)
# ===========================================

class Carro(Veiculo):
    """
    Classe que herda de Veiculo para representar carros.
    """
    def __init__(self, marca, modelo, ano, numero_portas, combustivel):
        super().__init__(marca, modelo, ano)
        self._numero_portas = numero_portas
        self._combustivel = combustivel
        """
        Construtor da classe Carro.
        TODO 8: Implemente o construtor:
        - Chame o construtor da classe pai (super().__init__(......))
        - Adicione os novos atributos COM EXATAMENTE ESSA NOMENCLATURA: 
                - _numero_portas 
                - _combustivel
        """
    @property
    def numeroportas(self):
        return self._numero_portas
    @numeroportas.setter
    def numeroportas(self, valor):
        if 2 <= valor <= 5:
            self._numero_portas = valor
        else:
            raise ValueError("O numero de portas tera que se 2 ou 5")
        

    @property
    def combustivel(self):
        return self.combustivel
    @combustivel.setter
    def combustivel(self,valor):
        if isinstance(valor, str) and valor.strip():
            self._combustivel = valor
    # TODO 9: Implemente getters e setters para os novos atributos
    # - getter e setter para numero_portas (para o setter, deve ser entre 2 e no maximo 5 portas)
    # - getter e setter para combustivel (para o setter, deve ser uma string não vazia)
    
    def __str__(self):
        """
        Método especial para representação em string. >> (JÁ ESTA IMPLEMENTADO. NÃO ALTERE.) <<
        """
        status = "Ligado" if self.ligado else "Desligado"
        return f"Carro: {self.marca} {self.modelo} ({self.ano}) - {self.numero_portas} portas - {self.combustivel} - {status}"

    
    # TODO 10: Implemente um método específico para carros
    def obter_informacoes_detalhadas(self):
        """
        Retorna informações detalhadas do carro.
        RETORNE: "Portas: [numero_portas] - Combustível: [combustivel] - Quilometragem: [quilometragem] km"
        DICA: Use self.quilometragem para acessar a quilometragem herdada da classe pai
        """
        return f"Portas: {self.numero_portas} - Combustível: {self.combustivel} - Quilometragem: {self.quilometragem} km"


# ===========================================
# QUESTÃO 3: HERANÇA - MOTO (2.0 pontos)
# ===========================================

class Moto(Veiculo):
    """
    Classe que herda de Veiculo para representar motos.
    """
    def __init__(self, marca, modelo, ano, cilindrada, tipo):
        super().__init__(marca, modelo, ano)
        self._cilindrada = cilindrada
        self._tipo = tipo
        """
        Construtor da classe Moto.
        TODO 11: Implemente o construtor:
        - Chame o construtor da classe pai (super().__init__(......))
        - Adicione os novos atributos COM EXATAMENTE ESSA NOMENCLATURA: 
                - _cilindrada 
                - _tipo
        """

    @property
    def cilindrada(self):
        return self._cilindrada
    @cilindrada.setter
    def cilindrada(self,valor):
        if valor > 0:
            self.cilindrada = valor
        else:
            raise ValueError("O valor nao pode ser 0")
    
    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self,valor):
        if isinstance(valor, str) and valor.strip():
            self.tipo = valor
        else:
            raise ValueError("Nao pode estar vazia")
    # TODO 12: Implemente getters e setters para os novos atributos
    # - getter e setter para cilindrada (para o setter, deve ser > 0 )
    # - getter e setter para tipo (para o setter, deve ser uma string não vazia (exemplo: "Naked", "Esportiva", "Custom"))
    

    #Aqui eu ja implementei o metodo especial para representação em string.
    def __str__(self):
        """
        Método especial para representação em string. (JÁ ESTÁ IMPLEMENTADO. NÃO ALTERE!)
        """
        status = "Ligado" if self.ligado else "Desligado"
        return f"Moto: {self.marca} {self.modelo} ({self.ano}) - {self.cilindrada}cc - {self.tipo} - {status}"

    
    # TODO 13: Implemente um método específico para motos
    def obter_informacoes_tecnica(self):
        """
        Retorna informações técnicas da moto.
        RETORNE : "Cilindrada: [cilindrada]cc - Tipo: [tipo] - Quilometragem: [quilometragem] km"
        DICA: Use self.quilometragem para acessar a quilometragem da classe pai
        """
        return f"Cilindrada: {self.cilindrada}cc - Tipo: {self.tipo} - Quilometragem: {self._quilometragem} km"


# ===========================================
# QUESTÃO 4: POLIMORFISMO - GARAGEM (2.0 pontos)
# ===========================================

class Garagem:
    """
    Classe para gerenciar uma garagem com diferentes tipos de veículos.
    AQUI NÃO PRECISA CHAMAR O CONSTRUTOR DA CLASSE PAI.
    """
    
    def __init__(self, nome):
        self.nome = nome
        self.veiculos = []
        """
        Construtor da classe Garagem.
        TODO 14: Implemente o seguinte no construtor:
        - Inicialize o atributo: nome 
        - Inicialize uma LISTA vazia para armazenar os veículos. nao precisa ser um atributo privado.
        """
    
    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)
        """
        Adiciona um veículo à garagem.
        TODO 15: Implemente a lógica para adicionar um veículo à lista
        """
        
    
    def listar_veiculos(self):
        print(f"O nome da Garagem e {self.nome}")
        for veiculo in self.veiculos:
            print(f"{veiculo}")

        """
        Lista todos os veículos da garagem.
        TODO 16: Implemente a lógica para imprimir todos os veículos
        Use polimorfismo - cada tipo de veículo terá sua própria representação
        Printe o nome da garagem antes de imprimir os veículos.
        Crie uma estrutura FOR para percorrer a lista de veículos e printar todos no terminal.
        """
    
    def buscar_veiculo_por_marca(self, marca):
            for veiculo in self.veiculos:
                if veiculo.marca.lower() == marca.lower():
                    return True
                else:
                    return f"Resultado errado"
                
    """
        Busca um veículo pela marca.
        TODO 17: Implemente a busca e retorne o primeiro veículo encontrado
        Crie uma estrutura FOR para percorrer a lista de veículos e buscar o veículo pela marca.
        DICA: use o .lower() para comparar a marca do veículo com a marca buscada.
        Se encontrado, retorne o veículo.
        Se não encontrado, retorne None ou "Marca não encontrada".
    """
    
    
    def ligar_veiculo(self, marca):
        if self.buscar_veiculo_por_marca(marca):
            print("Ligado")
        else:
            print("Veiculo nao encontrado na garagem")

        """
        Liga um veículo pela marca.
        TODO 18: Implemente a lógica:
        - Busque o veículo pela marca (use o metodo buscar_veiculo_por_marca() ja criado)
        - Se encontrado, tente ligá-lo
        - Se ja estiver ligado, retorne "Veículo já está ligado"
        - Se não encontrado, retorne "Veículo não encontrado na garagem"
        - Fique a vontade para criar uma mensagem legal.
        """
    
    def desligar_veiculo(self, marca):
        if self.buscar_veiculo_por_marca(marca):
            Veiculo.desligar()
            print("Veiculo desligado")
        else:
            print("Veiculo Nao encontrado na garagem")
        """
        Desliga um veículo pela marca.
        TODO 19: Implemente a lógica:
        - Busque o veículo pela marca (use o metodo buscar_veiculo_por_marca() ja criado)
        - Se encontrado, tente desligá-lo (mensagem de retorno: "Veículo desligado com sucesso!")
        - Se ja estiver desligado, retorne "Veículo já estava desligado"
        - Se não encontrado pela marca, retorne "Veículo não encontrado na garagem"
        - Fique a vontade para criar uma mensagem legal.
        """
    
    # TODO 20: Implemente um método estático para validar nome da garagem
    # O método deve verificar se o nome da garagem é válido (não vazio e sem números)
    # Dica1: use a função .isalpha() para verificar se o nome da garagem é apenas letras.
    # Dica2: use a função .strip() para remover espaços em branco.
    # Dica3: use isinstance(nome, str) para verificar se o nome é uma string.
    # Implemente a logica que quiser, mas deve retornar True se o nome da garagem for válido, False caso contrário.
    @staticmethod
    def validar_nome_garagem(nome):
        if isinstance(nome, str) and len(nome.strip()) > 0 and nome.replace(" ", "").isalpha():
            return True
        return False

        """
        Valida se o nome da garagem é válido (não vazio e sem números).
        """
        
    

    #Aqui eu ja implementei o metodo de classe para criar garagem de exemplo.
    @classmethod
    def criar_garagem_exemplo(cls):
        """
        Aqui eu implementei uma garagem de exemplo com alguns veículos.(JA ESTA IMPLEMENTADO. NÃO ALTERE.)
        """
        garagem = cls("Garagem Central")
        
        # Adicionando veículos de exemplo
        veiculo1 = Carro("Honda", "Civic", 2021, 4, "Flex")
        veiculo2 = Moto("Yamaha", "Fazer", 2020, 250, "Naked")
        veiculo3 = Carro("Ford", "Focus", 2019, 4, "Gasolina")
        veiculo4 = Moto("Kawasaki", "Ninja", 2022, 600, "Esportiva")
        
        garagem.adicionar_veiculo(veiculo1)
        garagem.adicionar_veiculo(veiculo2)
        garagem.adicionar_veiculo(veiculo3)
        garagem.adicionar_veiculo(veiculo4)
        
        return garagem

# ===========================================
# PARTE 5: TESTE DO SISTEMA < NÃO OBRIGATORIO IMPLEMENTAR > DEIXE PARA DIA DA CORRECAO 
# SE QUISER PODE IMPLEMENTAR, PARA TESTAR SEU CODIGO.
# ===========================================

def testar_sistema():

    """
    Função para testar o sistema implementado.
    TODO 21: Implemente os testes:
    1. Crie uma garagem
    
    2. Adicione veículos de diferentes tipos

    3. Teste ligar e desligar veículos

    4. Liste os veículos

    5. Teste buscas
    
    """
    m = Garagem.criar_garagem_exemplo()
    m.ligar_veiculo("Civic")
    m.desligar_veiculo("Civic")

# ===========================================
# EXECUÇÃO PRINCIPAL
# ===========================================

if __name__ == "__main__":
    print("=== PROVA P1 - ORIENTAÇÃO A OBJETOS ===")
    print("Complete todas as implementações marcadas com TODO")
    print("Execute testar_sistema() para testar sua implementação")
    print("=" * 40)
    
    # Descomente a linha abaixo para testar

#testar_sistema()
veiculo1=Carro('Honda','Civic',2021,4,'Gas')
veiculo2 = Moto("Yamaha", "Fazer", 2020, 250, "Naked")
garagem=Garagem('Manu')
garagem.adicionar_veiculo('veiculo1')
garagem.adicionar_veiculo('veiculo2')
print(veiculo1.marca)

