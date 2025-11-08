from notificador import Notificador
from noti_email import NotificadorEmail
from noti_log import NotificadorLog
from noti_whats import NotificadorWhatsapp
from noti_sms import NotificadorSMS
class Gerenciadordenotificacoes:
    def __init__(self, notificadores:list[Notificador]):
        self.notificador = notificadores
    def enviar_todos(self, mensagem):
        for notificador in self.notificador:
            notificador.enviar(mensagem)


#exemplo de Uso:
email = NotificadorEmail()
sms = NotificadorSMS()
zap = NotificadorWhatsapp()
log = NotificadorLog()

gerenciador = Gerenciadordenotificacoes([email, sms, zap, log])
gerenciador.enviar_todos("Sistema em manutenção as 22H, estao todos")


