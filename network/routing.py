from network.node import Node

class Grafo:
    def __init__(self):
        self.nodos: dict[str,Node] = {}

    def agregar_nodo(self,valor: str) -> None:
        nodo = Node(valor)
        self.nodos[valor] = nodo

    def construir_red(self, nodos: dict[str,list[str]]) -> None:
        for nombre,vecino in nodos.items():
            self.agregar_nodo(nombre)
            nodo = self.nodos.get(nombre)
            nodo.vecinos = vecino