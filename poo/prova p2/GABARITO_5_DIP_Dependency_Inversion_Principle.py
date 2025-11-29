"""
================================================================================
GABARITO - SIMULADO P2 - PROGRAMAÇÃO ORIENTADA A OBJETOS
Professor: Tiago Castro
Turma: 4º Período B - Engenharia de Software
================================================================================

PRINCÍPIO: DEPENDENCY INVERSION PRINCIPLE (DIP)
VALOR: 3,0 pontos

SOLUÇÃO CORRETA
================================================================================
"""

from abc import ABC, abstractmethod
from typing import List

# ============================================================================
# SOLUÇÃO APLICANDO O DIP
# ============================================================================
# 
# Agora NotificacaoService depende de uma abstração (Notificador),
# não de implementações concretas. Isso permite:
# - Adicionar novos canais sem modificar NotificacaoService
# - Testar facilmente com mocks
# - Trocar implementações facilmente
#
# ============================================================================

class Notificador(ABC):
    """
    Interface/abstração que define o contrato para qualquer canal de notificação.
    Módulos de alto nível dependem desta abstração, não de implementações concretas.
    """
    @abstractmethod
    def enviar(self, destinatario: str, mensagem: str):
        """
        Envia uma notificação para o destinatário.
        
        Args:
            destinatario: Endereço/número do destinatário
            mensagem: Mensagem a ser enviada
        """
        pass


class EmailService(Notificador):
    """
    Implementação concreta de Notificador para envio de emails.
    Agora implementa a interface, não é mais uma classe independente.
    """
    def enviar(self, destinatario: str, mensagem: str):
        """Envia email para o destinatário"""
        print(f"Enviando email para {destinatario}: {mensagem}")
        # Código real de envio de email aqui
        # Pode usar SMTP, API do Gmail, SendGrid, etc


class SMSService(Notificador):
    """
    Implementação concreta de Notificador para envio de SMS.
    Agora implementa a interface, não é mais uma classe independente.
    """
    def enviar(self, destinatario: str, mensagem: str):
        """Envia SMS para o número"""
        print(f"Enviando SMS para {destinatario}: {mensagem}")
        # Código real de envio de SMS aqui
        # Pode usar Twilio, AWS SNS, etc


class NotificacaoService:
    """
    Classe de alto nível que agora depende da ABSTRAÇÃO (Notificador),
    não de implementações concretas (EmailService, SMSService).
    
    Recebe notificadores via INJEÇÃO DE DEPENDÊNCIA no construtor.
    """
    def __init__(self, notificadores: List[Notificador]):
        """
        Recebe uma lista de notificadores via construtor.
        Depende da abstração, não de classes concretas!
        """
        self.notificadores = notificadores
    
    def notificar(self, destinatarios: dict, mensagem: str):
        """
        Notifica usando todos os canais disponíveis.
        
        Args:
            destinatarios: Dicionário com chaves 'email', 'telefone', etc
            mensagem: Mensagem a ser enviada
        """
        for notificador in self.notificadores:
            # Determina o destinatário baseado no tipo de notificador
            if isinstance(notificador, EmailService):
                if 'email' in destinatarios:
                    notificador.enviar(destinatarios['email'], mensagem)
            elif isinstance(notificador, SMSService):
                if 'telefone' in destinatarios:
                    notificador.enviar(destinatarios['telefone'], mensagem)
            else:
                # Para novos tipos, pode usar um padrão ou mapeamento
                # Por exemplo, se tiver 'whatsapp' no dicionário
                tipo = type(notificador).__name__.replace('Service', '').lower()
                if tipo in destinatarios:
                    notificador.enviar(destinatarios[tipo], mensagem)


# ============================================================================
# EXEMPLO DE USO
# ============================================================================

if __name__ == "__main__":
    # Criar serviços concretos
    email_service = EmailService()
    sms_service = SMSService()
    
    # Injetar dependências no construtor (INJEÇÃO DE DEPENDÊNCIA)
    notificacao = NotificacaoService([email_service, sms_service])
    
    # Usar o serviço
    destinatarios = {
        'email': 'user@email.com',
        'telefone': '123456789'
    }
    notificacao.notificar(destinatarios, "Mensagem importante")
    
    print("\n" + "="*60)
    print("EXTENSIBILIDADE: Adicionar novo canal SEM MODIFICAR NotificacaoService!")
    print("="*60 + "\n")
    
    # ========================================================================
    # EXTENSIBILIDADE: Adicionar novo canal sem modificar NotificacaoService
    # ========================================================================
    
    class WhatsAppService(Notificador):
        """Novo canal de notificação - apenas implementa a interface!"""
        def enviar(self, destinatario: str, mensagem: str):
            print(f"Enviando WhatsApp para {destinatario}: {mensagem}")
            # Código real de envio via WhatsApp API
    
    class PushNotificationService(Notificador):
        """Outro novo canal - apenas implementa a interface!"""
        def enviar(self, destinatario: str, mensagem: str):
            print(f"Enviando Push Notification para {destinatario}: {mensagem}")
            # Código real de push notification
    
    # Criar novos serviços
    whatsapp_service = WhatsAppService()
    push_service = PushNotificationService()
    
    # Usar com os novos canais - SEM MODIFICAR NotificacaoService!
    notificacao_extendida = NotificacaoService([
        email_service,
        sms_service,
        whatsapp_service,
        push_service
    ])
    
    destinatarios_extendidos = {
        'email': 'user@email.com',
        'telefone': '123456789',
        'whatsapp': '+5511999999999',
        'push': 'device_token_123'
    }
    notificacao_extendida.notificar(destinatarios_extendidos, "Nova mensagem!")
    
    print("\n" + "="*60)
    print("TESTABILIDADE: Fácil criar mocks para testes!")
    print("="*60 + "\n")
    
    # ========================================================================
    # TESTABILIDADE: Criar mocks para testes
    # ========================================================================
    
    class MockNotificador(Notificador):
        """Mock para testes - não envia notificações reais"""
        def __init__(self):
            self.notificacoes_enviadas = []
        
        def enviar(self, destinatario: str, mensagem: str):
            self.notificacoes_enviadas.append({
                'destinatario': destinatario,
                'mensagem': mensagem
            })
            print(f"[MOCK] Notificação registrada: {destinatario} - {mensagem}")
    
    # Testar com mock
    mock_notificador = MockNotificador()
    notificacao_teste = NotificacaoService([mock_notificador])
    notificacao_teste.notificar({'email': 'test@test.com'}, "Teste")
    
    print(f"\nNotificações enviadas no mock: {len(mock_notificador.notificacoes_enviadas)}")
    print(f"Conteúdo: {mock_notificador.notificacoes_enviadas}")

