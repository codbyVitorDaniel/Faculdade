from notificador import Notificador
class NotificadorEmail(Notificador):
    def enviar(self, mensagem):
        print(f'Enviando [Email] com a mensagem {mensagem}')
    