from notificador import Notificador

class NotificadorWhatsapp(Notificador):
    def enviar(self, mensagem):
        print(f'Enviando [ZAP] com a mensagem {mensagem}')
