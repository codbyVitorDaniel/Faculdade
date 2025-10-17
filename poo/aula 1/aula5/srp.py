#solid
#srp - Single Responsibilite Principle

class RelatorioFinanceiro:
    def calcular_dados(self, dados):
        #logica para calcular dados financeiros
        #Processamento das informaçoes
        pass
class RelatorioArquivos:
    def salvar_dados(self,nome_arquivos):
        #logica para salvar o relatorio em um arquivo
        #I/O gerenciamento de arquivos
        pass
class RelatorioEmail:
    def enviar_email(self,destinatario):
        #Logica para enviar o relatorio por email
        pass

#Forma de uso
relatorio = RelatorioFinanceiro()
relatorioArquivo = RelatorioArquivos()
relatorio_envio = RelatorioEmail()

relatorio_pronto = relatorio.calcular_dados("ABC")
relatorioArquivo.salvar_dados(relatorio_pronto)
relatorio_envio.enviar_email(relatorio_pronto)

