from abc import ABC, abstractmethod

class Exportador(ABC):
    @abstractmethod
    def exportar(self, dados):
        pass

class ExportadorCSV(Exportador):
    def exportar(self, dados):
        print("Exportando dados em CSV...")

class ExportadorPDF(Exportador):
    def exportar(self, dados):
        print("Exportando dados em PDF...")
