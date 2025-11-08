from abc import ABC, abstractmethod

class Notificador(ABC):
    def enviar(self, mensagem):
        pass
    