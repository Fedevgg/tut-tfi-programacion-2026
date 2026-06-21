"""
Redes y Comunicación
Crear un red de ocho nodos que muestre una relación
direccionada, de manera que cada nodo sólo pueda tener
comunicación directa con otros 2 nodos.
"""

NODE_COUNT = 8


def build_network() -> dict[int, list[int]]:
    """
    Builds a directed network of eight nodes
    Returns:
        dict[int, list[int]]: Each node mapped to its two direct connections
    """
    network = {}
    for node in range(1, NODE_COUNT + 1):
        network[node] = [
            (node % NODE_COUNT) + 1,
            ((node + 1) % NODE_COUNT) + 1,
        ]
    return network


def print_network(network: dict[int, list[int]]) -> None:
    """
    Prints the network
    Args:
        network (dict[int, list[int]]): The network
    """
    print("Red de comunicación (relación direccionada):")
    for node, connections in network.items():
        targets = ", ".join(str(target) for target in connections)
        print(f"Nodo {node} → {targets}")


def main():
    network = build_network()
    print_network(network)


if __name__ == "__main__":
    main()
