import matplotlib.pyplot as plt
import networkx as nx


while True:
    try:
        quantidade = int(input("Diga quantas cidades você quer:\nR: "))
        if quantidade <= 0:
            print("Informe um número inteiro positivo.")
            continue
        break
    except ValueError:
        print("Digite um número inteiro válido.")


cidades = []
existentes = set()
while len(cidades) < quantidade:
    nome = input(f"Digite o nome da cidade {len(cidades)+1}: ").strip()
    if not nome:
        print("O nome da cidade não pode ser vazio.")
        continue
    if nome in existentes:
        print("Cidade já informada. Digite um nome diferente.")
        continue
    cidades.append(nome)
    existentes.add(nome)


G = nx.DiGraph()
G.add_nodes_from(cidades)


auto = input("\nDeseja ligar em cadeia (cidade 1 → 2 → 3 ...), perguntando o peso de cada ligação? (s/n): ").strip().lower()

estradas = []
if auto == "s":
    if len(cidades) < 2:
        print("\nNão há cidades suficientes para ligar em cadeia.")
    else:
        print("\nInforme os pesos para cada ligação sequencial:")
        for i in range(len(cidades) - 1):
            origem = cidades[i]
            destino = cidades[i + 1]
            while True:
                peso_str = input(f"Peso de '{origem}' → '{destino}': ").strip()
                try:
                    peso = float(peso_str)
                    if peso <= 0:
                        print("O peso deve ser um número positivo.")
                        continue
                    break
                except ValueError:
                    print("Peso inválido. Use número (ex.: 3 ou 2.5).")
            estradas.append((origem, destino, {"weight": peso}))
        print(f"\nForam criadas {len(estradas)} ligações em cadeia.")
else:

    print("\nAgora, digite as estradas entre as cidades.")
    print("Formato: origem destino peso (ex.: Armazem CidadeA 5)")
    print("Observação: um peso pode ser decimal (ex.: 2.5).")
    print("Digite 'fim' para encerrar.\n")

    while True:
        entrada = input("Estrada: ").strip()
        if entrada.lower() == "fim":
            break
        partes = entrada.split()
        if len(partes) != 3:
            print("Entrada inválida. Use exatamente 3 itens: origem destino peso.")
            continue

        origem, destino, peso_str = partes

        if origem not in existentes:
            print(f"Origem '{origem}' não está na lista de cidades cadastradas.")
            continue
        if destino not in existentes:
            print(f"Destino '{destino}' não está na lista de cidades cadastradas.")
            continue

        try:
            peso = float(peso_str)
            if peso <= 0:
                print("O peso deve ser um número positivo.")
                continue
        except ValueError:
            print("Peso inválido. Use número (ex.: 3 ou 2.5).")
            continue

        estradas.append((origem, destino, {"weight": peso}))


if estradas:
    G.add_edges_from(estradas)
else:
    print("\nNenhuma estrada adicionada. O grafo terá apenas os nós.")


pos = nx.circular_layout(G) if len(G) <= 8 else nx.spring_layout(G, seed=42)

nx.draw(
    G, pos,
    with_labels=True,
    node_color="lightblue",
    node_size=1500,
    font_size=10,
    arrows=True,
    arrowsize=20,
    edge_color="#555"
)

labels = nx.get_edge_attributes(G, "weight")
labels_fmt = {e: (int(w) if float(w).is_integer() else w) for e, w in labels.items()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_fmt)

plt.tight_layout()
plt.show()
