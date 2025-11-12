import matplotlib.pyplot as plt
import networkx as nx

quantidade = int(input("Diga quantas cidades você quer:\nR: "))
cidades = []
while quantidade > 0:
    digite = input("Digite o nome da cidade: ")
    cidades.append(digite)
    quantidade -= 1  

G = nx.DiGraph()
G.add_nodes_from(cidades)

