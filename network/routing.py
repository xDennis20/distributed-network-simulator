from network.node import Node

class Grafo:
    def __init__(self):
        self.nodos: dict[str,Node] = {}

    def agregar_nodo(self,valor: str) -> None:
        nodo = Node(valor)
        self.nodos[valor] = nodo
