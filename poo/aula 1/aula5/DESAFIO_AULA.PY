# ATIVIDADE
# ESTE CODIGO Não segue os principios SRP, OCP e LSP
# REFAÇA O CODIGO SEGUINDO ESTES PRINCIPIOS DE PROJETO DE SOFTWARE


#Classe que gerencia notificações | QUEBRANDO O PRINCIPIO SRP
class EnviarEmail:
    def enviar(self, mensagem):
        print(f"Enviando email: {mensagem}")

class EnviarSMS:
    def enviar(self, mensagem):
        print(f"Enviando SMS: {mensagem}")

class EnviarWhatsApp:
    def enviar(self, mensagem):
        print(f"Enviando WhatsApp: {mensagem}")


# Função que decide o tipo de envio com if/elif | QUEBRANDO O PRINCIPIO OCP

def enviar_notificacao(notificador, mensagem):
    notificador.enviar(mensagem)

email = EnviarEmail()
sms = EnviarSMS()
whatsapp = EnviarWhatsApp()

enviar_notificacao(email, "Mensagem via Email")
enviar_notificacao(sms, "Mensagem via SMS")
enviar_notificacao(whatsapp, "Mensagem via WhatsApp")


# Exemplo de uso | QUEBRANDO O PRINCIPIO LSP
mensagem = "Olá! Você tem uma nova mensagem."

enviar_notificacao(EnviarEmail(), mensagem)
enviar_notificacao(EnviarSMS(), mensagem)
