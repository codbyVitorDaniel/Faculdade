class Usuario:
    #Atributos de classe (compartilhado com todos os Objetos)
    usuario = []
    
    def __init__(self, nome):
        self.nome = nome
        #sempre que um novo usuario e criado, ele e adicionado a lista
        Usuario.usuario.append(self)
    def monstrar_nome(self):
        return f"nome:{self.nome}"
    
    @classmethod
    def listar_usuarios(cls):
        #Metodo de classe >acessa dados compartilhados
        #retorna a quantidade de objetos criados
        return len(cls.usuario)

user1 = Usuario("Vitor")
user2 = Usuario("Joao")
user3 = Usuario("Theo")

print(user1.nome)
print("="*30)
print(f" O total de usuarios:{Usuario.listar_usuarios()}")
print("="*30)