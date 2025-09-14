from random import randint

#Class Base
class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self._vida = vida
    # Getter (permite ler a vida)
    def get_vida(self):
        return self._vida
    def set_vida(self, valor):
        if valor <0:
            self._vida = 0
        
        elif valor > 100: #limite (opcional)
            self._vida = 100
        else:
            self._vida = valor

    vida = property(get_vida, set_vida)
    def atacar(self):
    #metodo Generico - Subercrito pelas subclasses
        return 0

#Classes que herdam de personagens 
class Guerreiro(Personagem):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida)
        self.forca = forca
    
    def atacar(self):
        ataque = self.forca - randint(0,30)
        print(f"{self.nome} golpeou com uma espada causando {ataque} de dano.")
        return max (0, ataque)
class Mago(Personagem):
    def __init__(self, nome, vida, magia):
        super().__init__(nome, vida)
        self.magia = magia
    
    def atacar(self):
        ataque = self.magia - randint(0, 30)
        print(f"{self.nome} Lançou uma magia causando {ataque} de Dano.")
        return max (0,ataque)
    
#Polimorfismo
personagens = [
    Guerreiro("Meliodas", 200, 150),
    Mago("Merlin", 100, 180)
]

for p in personagens:
    p.atacar() #O metodo se adapta ao Objeto



#Criando os personagens 
print("=-==-=-=-=- Bem Vindo a Batalha no terminal")
print("-=-= Crie dois personagens--")
print("--Mago ou Guerreiro --")
print("---------------")

listaJogadores = []

for q  in range(0 ,2):
    classePersonagem = int(input("Digite [1] - Guerreiro \nDigite [2] -Mago\nR: "))

    nome = input("Digite o nome do personagem:")
    vida = int(input(f"{nome} Possuira Vida:"))
    if classePersonagem == 1:
        forca = int(input(f"{nome} Possuira Força:"))
        jogador = Guerreiro(nome, vida, forca)
    elif classePersonagem == 2:
        magia = int(input(f"{nome} Possuira Magia:"))
        jogador = Mago(nome , vida, magia)
    
    listaJogadores.append(jogador)
    print("-------------")

# Jogadores
jogador1 = listaJogadores[0]
jogadores2 = listaJogadores[1]

print("=-=-=-==-=- Inicio do combate  =-=-=-==-")
print(f"{jogador1.nome} VS {jogadores2.nome}")
print("-+.-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

#Loop da batalha
while True:
    #Turno do jogador1
    if input(f"{jogador1.nome} Deseja Atacar? [s/n]: ") in "Ss":
        ataque = jogador1.atacar() # << Polimorfismo 
        jogadores2.vida -= ataque
        print(f"{jogadores2.nome} Agora tem{jogadores2.vida} de vida.")
        print("<------------------>")

        if jogadores2.vida <= 0:
            print(f"{jogadores2.vida} esta morto. {jogador1.nome} VOCE MORREU.")
            break
    else:
        print(f"{jogador1.nome} Passou a vez!")
    
    #turno do jogador 2

    if input(f"{jogadores2.nome} Deseja Atacar? [s/n]: ") in "Ss":
        ataque = jogadores2.atacar() # << Polimorfismo 
        jogador1.vida -= ataque
        print(f"{jogador1.nome} Agora tem{jogador1.vida} de vida.")
        print("<------------------>")

        if jogador1.vida <= 0:
            print(f"{jogador1.vida} esta morto. {jogadores2.nome} VOCE MORREU.")
            break
    else:
        print(f"{jogadores2.nome} Passou a vez!")


print("=========================")
print("----- Fim de jogo ----")
print("==========================")