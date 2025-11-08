from notificador import Notificador
from datetime import datetime



class NotificadorLog(Notificador):
    def enviar(self, mensagem):
        timestap = self._generate_timestap()
        with open ('log.txt', 'a') as file:
            file.write(f' {timestap} - [LOG] {mensagem}')
    
    def _generate_timestap(self):
        return datetime.now().strftime("%d%m%Y-%H:%M:%S")