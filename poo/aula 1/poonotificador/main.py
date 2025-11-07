from abc import ABC, abstractmethod

class Notificador(ABC):
    def enviar(self, mensagem):
        pass


class NotificadorEmail(Notificador):
    def enviar(self, mensagem):
        print(f'Enviando [Email] com a mensagem {mensagem}')
    
class NotificadorSMS(Notificador):
    def enviar(self, mensagem):
        print(f'Enviando [SMS] com a mensagem {mensagem}')

class NotificadorWhatsapp(Notificador):
    def enviar(self, mensagem):
        print(f'Enviando [ZAP] com a mensagem {mensagem}')

class NotificadorLog(Notificador):
    def enviar(self, mensagem):
        with open ('log.txt', 'a') as file:
            file.write('[LOG] {mensagem}')


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
