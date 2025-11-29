"""
================================================================================
GABARITO - SIMULADO P2 - PROGRAMAÇÃO ORIENTADA A OBJETOS
Professor: Tiago Castro
Turma: 4º Período B - Engenharia de Software
================================================================================

PRINCÍPIO: SINGLE RESPONSIBILITY PRINCIPLE (SRP)
VALOR: 1,0 ponto

SOLUÇÃO CORRETA
================================================================================
"""

# ============================================================================
# SOLUÇÃO APLICANDO O SRP
# ============================================================================
# 
# Cada classe agora tem uma única responsabilidade:
# - Pedido: apenas gerencia dados e calcula total
# - PedidoRepository: apenas persiste dados
# - EmailService: apenas envia emails
# - RelatorioService: apenas gera relatórios
#
# ============================================================================

class Pedido:
    """
    Classe responsável APENAS por representar os dados do pedido
    e calcular o total. Não se preocupa com persistência, comunicação ou relatórios.
    """
    def __init__(self, numero, cliente, itens):
        self.numero = numero
        self.cliente = cliente
        self.itens = itens
    
    def calcular_total(self):
        """Calcula o total do pedido"""
        total = 0
        for item in self.itens:
            total += item['preco'] * item['quantidade']
        return total


class PedidoRepository:
    """
    Classe responsável APENAS por persistir pedidos no banco de dados.
    Se a forma de salvar mudar, apenas esta classe precisa ser alterada.
    """
    def salvar(self, pedido):
        """Salva o pedido no banco de dados"""
        print(f"Salvando pedido {pedido.numero} no banco de dados...")
        # Código de conexão com banco aqui
        # Se precisar mudar de SQLite para PostgreSQL, apenas aqui muda


class EmailService:
    """
    Classe responsável APENAS por enviar emails.
    Se a forma de envio mudar (ex: de SMTP para API), apenas esta classe muda.
    """
    def enviar_confirmacao(self, pedido):
        """Envia email de confirmação para o cliente"""
        total = pedido.calcular_total()
        print(f"Enviando email para {pedido.cliente} confirmando pedido {pedido.numero} no valor de R$ {total:.2f}")
        # Código de envio de email aqui
        # Se precisar mudar de Gmail para SendGrid, apenas aqui muda


class RelatorioService:
    """
    Classe responsável APENAS por gerar relatórios.
    Se o formato do relatório mudar (PDF, Excel, etc), apenas esta classe muda.
    """
    def gerar(self, pedido):
        """Gera relatório do pedido"""
        print(f"Gerando relatório do pedido {pedido.numero}...")
        # Código de geração de relatório aqui
        # Se precisar mudar de PDF para Excel, apenas aqui muda


# ============================================================================
# EXEMPLO DE USO
# ============================================================================

if __name__ == "__main__":
    # Criar pedido
    pedido = Pedido(1, "joao@email.com", [{"preco": 10.0, "quantidade": 2}])
    total = pedido.calcular_total()
    print(f"Total do pedido: R$ {total:.2f}")
    
    # Salvar no banco (responsabilidade do Repository)
    repository = PedidoRepository()
    repository.salvar(pedido)
    
    # Enviar email (responsabilidade do EmailService)
    email_service = EmailService()
    email_service.enviar_confirmacao(pedido)
    
    # Gerar relatório (responsabilidade do RelatorioService)
    relatorio_service = RelatorioService()
    relatorio_service.gerar(pedido)

