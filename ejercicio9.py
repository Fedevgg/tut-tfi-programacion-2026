# Redes y Comunicación
# Crear un red de ocho NODES que muestre una relación
# direccionada, de manera que cada nodo sólo pueda tener
# comunicación directa con otros 2 NODES

import sys

import matplotlib.pyplot as plt
import networkx as nx


def generate_sample_network():
    """
    Generates a sample network with 8 nodes and 2 outgoing connections per node
    """
    NODES = 8
    G = nx.DiGraph()
    G.add_nodes_from(range(1, NODES + 1))

    for nodo in range(1, NODES + 1):
        G.add_edge(nodo, nodo % NODES + 1)
        G.add_edge(nodo, (nodo + 1) % NODES + 1)

    pos = nx.circular_layout(G)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="lightblue",
        node_size=800,
        font_size=12,
        arrows=True,
        arrowsize=15,
    )
    plt.title("Red de 8 NODOS (2 conexiones directas salientes por nodo)")

    if "google.colab" in sys.modules:
        plt.show()
    else:
        plt.savefig("network.png", dpi=150, bbox_inches="tight")
        print("Gráfico guardado en network.png")


if __name__ == "__main__":
    generate_sample_network()
